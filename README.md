A simulated QuickBooks GL data extractor for multiple companies using Python &amp; Pandas.
![Workflow Overview](flowchart.gif)

🧾 QuickBooks GL Extractor (Demo Portfolio Project)
This is a demo project that simulates how to extract General Ledger (GL) data from multiple companies using the QuickBooks API. It’s designed as a portfolio piece to show readiness for real-world QuickBooks integrations.

🚀 Key Features
Parses GL data from multiple companies (simulated API)

Exports clean financial entries to CSV format

Designed for automation & scalability

Future-ready structure for real QuickBooks API integration

📂 Project Structure
gl_sample_data.json — Simulated GL data for Company 1
gl_company_2.json — Simulated GL data for Company 2
qb_gl_api_client.py — Simulated API client
qb_gl_extractor.py — Main script that extracts and merges GL data
gl_report.csv — Output CSV with all financial transactions
README.md — Project documentation (this file)

🔧 Tech Stack
Python 3.x

Pandas

JSON

🧠 Simulated API Integration
Even though this project doesn't connect to the real QuickBooks API, it's built to mimic it:

qb_gl_api_client.py simulates API requests per company

Code is modular and can be easily swapped with real requests-based API logic

Designed with future OAuth2 token and endpoint compatibility in mind

Great foundation for both QuickBooks Online and Desktop integrations

🏁 Sample Output (CSV)
Company	Account Name	Account Number	Date	Description	Debit	Credit	Balance
Demo_Company_001	Bank Account	1020	2023-01-05	Office Supplies	200.0	0.0	200.0
Demo_Company_002	Credit Card	2050	2023-02-02	Software Subscription	0.0	300.0	-300.0
