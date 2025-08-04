import json
import time

def fetch_gl_report(company_id):
    """
    Simulates API call to QuickBooks to fetch GL report for a company.
    """
    print(f"🔌 Connecting to QuickBooks API for {company_id}...")
    time.sleep(1)

    filename = f"{company_id}.json"
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print(f"✅ Data received from {company_id}\n")
            return data
    except FileNotFoundError:
        print(f"❌ Data file {filename} not found.")
        return None
