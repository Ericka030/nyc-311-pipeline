# EDA analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("cleaned_311_data.csv")

# Display basic info
print("[INFO] DataFrame shape:", df.shape)
print("[INFO] Columns:", df.columns.tolist())
print("[INFO] Top complaint type:\n", df['complaint_type'].value_counts().head(10))

# Plot top 10 complaint type
plt.figure(figsize=(10, 6))
df['complaint_type'].value_counts().head(10).plot(kind='barh', color='skyblue')
plt.title('Top 10 Complaint Types')
plt.xlabel('Number of Complaints')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top_complaints.png")
#plt.show()

# Analyze complaint over time
# Convert created_date to datetime
df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')

# Drop rows where date conversion failed
df = df.dropna(subset=['created_date'])

# Group by date and count complaints
daily_complaints = df.groupby(df['created_date'].dt.date).size()

# Plot time series
plt.figure(figsize=(14, 6))
daily_complaints.plot()
plt.title("Daily Complaint Volume Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Complaints")
plt.tight_layout()
plt.savefig("daily_complaints_trend.png")
#plt.show()

# Top Complaint Volume by Borough
# Group by borough count complaints
borough_counts = df['borough'].value_counts()

# plt complaint volume by borough
plt.figure(figsize=(8, 5))
borough_counts.plot(kind='bar', color='skyblue')
plt.title("Complaint Volume by Borough")
plt.xlabel("Borough")
plt.ylabel("Number of Complaints")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("borough_complaints_bar.png")
plt.show()

print("\nComplaint counts by borough:\n", borough_counts)