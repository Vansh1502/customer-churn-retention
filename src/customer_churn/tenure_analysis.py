import pandas as pd

DATA_PATH = "data/processed/customer_churn_cleaned.csv"
df = pd.read_csv(DATA_PATH)

# Group customers by tenure
bins = [-1, 12, 24, 48, 72]
labels = [
    "0-12 months",
    "13-24 months",
    "25-48 months",
    "49-72 months"
]

df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=bins,
    labels=labels
)

# Calculate customer count and churn rate
result = df.groupby("TenureGroup", observed=False).agg(
    TotalCustomers=("Churn", "count"),
    ChurnedCustomers=("Churn", lambda x: (x == "Yes").sum())
)

result["ChurnRate"] = (
    result["ChurnedCustomers"] / result["TotalCustomers"] * 100
).round(2)

print("=" * 55)
print("CUSTOMER CHURN BY TENURE GROUP")
print("=" * 55)
print(result.to_string())

print("\nTenure analysis completed successfully!")
