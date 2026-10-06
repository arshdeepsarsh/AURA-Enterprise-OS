import os
import numpy as np
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()
magic_url: str = os.environ.get("SUPABASE_URL")
magic_key: str = os.environ.get("SUPABASE_KEY")
cloud_box: Client = create_client(magic_url, magic_key)

def check_my_paper():
    print("Yay! Paper Checker Machine 5000!")
    
    paper_story = "Supplier XYZ agrees to deliver 500 units of lithium-ion batteries by Q3. Penalty for delay is $5,000 per day."
    paper_name = "Supplier_XYZ_Contract_v1.pdf"
    
    print(f"Reading paper: {paper_name}")
    print("Asking AI robot to make shiny magic numbers...")
    
    magic_numbers = np.random.rand(768).tolist() 
    
    print("Putting paper into cloud treasure chest...")
    
    try:
        response = cloud_box.table("documents").insert({
            "document_name": paper_name,
            "content": paper_story,
            "embedding": magic_numbers
        }).execute()
        
        print("Yay! Paper stored in giant super brain!")
    except Exception as oopsie:
        print(f"Uh oh! Treasure chest said no: {oopsie}")

if __name__ == "__main__":
    check_my_paper()