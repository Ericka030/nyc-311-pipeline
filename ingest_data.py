import requests
import pandas as pd

# NYC 311 API endpoint
API_URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"

# Parameters
params ={
    "$limit": 5000,         # We'll start with 5000 records
    "$order": "created_date DESC"
}

# Request data
response = requests.get(API_URL, params=params)

# Check response
if response.status_code ==200:
    data = response.json()
    df = pd.DataFrame(data)
    print(" Data succesfully fetched!")
    print(df.head())
    df.to_csv("raw_311_data.csv", index=False)
    print("✅Data saved as raw_311_data.csv")
else:
    print("❌Failed to fetch data:", response.status_code)