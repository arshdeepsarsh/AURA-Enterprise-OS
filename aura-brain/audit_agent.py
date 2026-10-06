import os
import json
import requests
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Load Keys & Configure the Brain
load_dotenv()
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini Model
model = genai.GenerativeModel('gemini-1.5-flash')

JAVA_CORE_URL = "http://localhost:8080/api/v1/invoices"

def audit_with_llm(vendor, amount, invoice_number):
    """Passes the invoice data to the LLM for autonomous reasoning."""
    
    prompt = f"""
    You are the Chief Compliance AI for an enterprise. 
    Review this invoice:
    - Invoice Number: {invoice_number}
    - Vendor: {vendor}
    - Total Amount: ${amount}
    
    Corporate Rules:
    1. If the amount is over $10,000, status must be "FLAGGED_HIGH_VALUE".
    2. If the vendor name implies they are shady or unverified (e.g., "Unknown", "XYZ", "Test"), status must be "REJECTED".
    3. Otherwise, status is "APPROVED".
    
    You must respond ONLY with a valid JSON object in this exact format:
    {{"status": "YOUR_DECISION", "reason": "A 1-sentence explanation of your thought process."}}
    """
    
    # Send the prompt to the AI
    response = model.generate_content(prompt)
    
    # Clean and parse the AI's JSON response
    raw_text = response.text.replace("```json", "").replace("```", "").strip()
    return json.loads(raw_text)

def run_cognitive_audit():
    print("====== AURA BRAIN: COGNITIVE LLM AUDITOR ACTIVE ======")
    
    # 2. Fetch pending invoices from Java Ledger
    response = requests.get(JAVA_CORE_URL)
    if response.status_code != 200:
        print("[ERROR] Failed to fetch invoices from Core.")
        return

    invoices = response.json()
    print(f"[INFO] Fetched {len(invoices)} invoice(s). Initializing LLM context...\n")

    # 3. Process each invoice through the AI
    for inv in invoices:
        invoice_id = inv["id"]
        vendor = inv["vendorName"]
        amount = inv["totalAmount"]
        current_status = inv["status"]

        if current_status != "PENDING":
            continue

        print(f"[THINKING] LLM is analyzing Invoice #{inv['invoiceNumber']}...")
        
        # Call the Gemini AI Engine
        ai_decision = audit_with_llm(vendor, amount, inv['invoiceNumber'])
        
        new_status = ai_decision["status"]
        reason = ai_decision["reason"]

        print(f" -> AI Decision: {new_status}")
        print(f" -> AI Reasoning: {reason}")

        # 4. Transmit updated status back to Java Ledger
        update_url = f"{JAVA_CORE_URL}/{invoice_id}/status"
        patch_response = requests.patch(update_url, json={"status": new_status})

        if patch_response.status_code == 200:
            print(f" -> [SUCCESS] Ledger updated!\n")
        else:
            print(f" -> [ERROR] Failed to update Ledger.\n")

if __name__ == "__main__":
    run_cognitive_audit()