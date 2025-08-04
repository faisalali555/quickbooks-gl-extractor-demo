import pandas as pd
from qb_gl_api_client import fetch_gl_report

company_ids = ["gl_sample_data", "gl_company_2"]
all_rows = []

for company_id in company_ids:
    data = fetch_gl_report(company_id)
    if not data:
        continue

    for account in data['Rows']:
        account_name = account['Account']
        account_num = account['AccountNum']

        for txn in account['Transactions']:
            all_rows.append({
                "Company": data.get("Company", company_id),
                "Account Name": account_name,
                "Account Number": account_num,
                "Date": txn['TxnDate'],
                "Description": txn['Description'],
                "Debit": txn['Debit'],
                "Credit": txn['Credit'],
                "Balance": txn['Balance']
            })

df = pd.DataFrame(all_rows)
df.to_csv('gl_report.csv', index=False)
print("✅ Multi-company General Ledger report saved to gl_report.csv")
