import pandas as pd

# Load the raw csv
df = pd.read_csv("raw_311_data.csv")

print("Loaded", len(df), "rows and", len(df.columns), "columns")
print("First few complaints types:")
print(df['complaint_type'].value_counts().head())

# Drop rows missing key fields
df = df.dropna(subset =['created_date', 'complaint_type', 'borough'])

# Convert created_date to datetime
df['created_date'] = pd.to_datetime(df['created_date'])

# Create new column: date only (no time)
df['created_day'] = df['created_date'].dt.date

# Standardize column names (optional)
df.columns = df.columns.str.lower()

# Save cleaned data
df.to_csv("cleaned_311_data.csv", index=False)
print("Cleaned data saved as cleaned_311_data.csv")