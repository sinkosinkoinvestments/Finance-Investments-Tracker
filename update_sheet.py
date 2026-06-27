import os
import json
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# 1. Authenticate with Google Sheets
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds_json = json.loads(os.environ.get("GOOGLE_CREDENTIALS"))
creds = Credentials.from_service_account_info(creds_json, scopes=scopes)
client = gspread.authorize(creds)

# 2. Open the Sheet
SHEET_ID = os.environ.get("SHEET_ID")
sheet = client.open_by_key(SHEET_ID)
auto_tab = sheet.worksheet("Automated_Data")

# 3. Fetch RBA Cash Rate (Placeholder for your API call)
try:
    rba_rate = 0.0435 # Replace with requests.get() to your chosen API
except Exception as e:
    print(f"Error fetching rate: {e}")
    rba_rate = 0.0435

# 4. Update the Sheet
today = datetime.now().strftime("%Y-%m-%d")
auto_tab.update_acell('C2', rba_rate)
auto_tab.update_acell('D2', today)

print(f"Successfully updated spreadsheet on {today}")
