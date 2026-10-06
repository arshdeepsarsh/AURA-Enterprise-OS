import requests

def send_bill_to_friend():
    target_link = "http://localhost:8080/api/v1/invoices"
    
    bill_stuff = {
        "invoiceNumber": "INV-2026-001",
        "vendorName": "Supplier XYZ Ltd.",
        "totalAmount": 12500.50,
        "status": "PENDING"
    }
    
    print("Shooting paper bill to main computer!")
    print(f"Sending bill {bill_stuff['invoiceNumber']} now...")
    
    try:
        response = requests.post(target_link, json=bill_stuff)
        
        if response.status_code == 200:
            print("Yay! Main computer took the bill!")
            print("Got back:", response.json())
        else:
            print(f"Oh no! Main computer said no! Code: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Uh oh! Cannot find main computer! Is it turned on on port 8080?")

if __name__ == "__main__":
    send_bill_to_friend()