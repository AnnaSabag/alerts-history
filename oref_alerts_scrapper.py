import requests
import openpyxl
import pandas as pd

url = "https://alerts-history.oref.org.il/Shared/Ajax/GetAlarmsHistory.aspx"
params = {
    "lang": "he",
    "fromDate": "07.10.2023",
    "toDate": "30.10.2023",
    "mode": "0"
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://alerts-history.oref.org.il/"
}

response = requests.get(url, headers=headers, params=params)

# Check for empty or error
if response.status_code == 200 and response.text.strip():
    try:
        data = response.json()
        df = pd.DataFrame(data)
        print(df)
        df.to_excel("Alerts_History.xlsx", index=False, engine='openpyxl')
        print("Alerts saved to 'Alerts_History.xlsx'")
    except Exception as e:
        print("Failed to parse JSON:", e)
else:
    print(f"Request failed: {response.status_code}")
