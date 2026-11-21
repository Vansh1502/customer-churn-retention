import pandas as pd
from pathlib import Path

df = pd.read_csv("data/processed/customer_churn_cleaned.csv")

output = Path("reports/eda_summary.txt")

def churn_rate(column):
    return (
        df.groupby(column, observed=True)["Churn"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .round(2)
        .sort_values(ascending=False)
    )

# Tenure groups
df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, 72],
    labels=["0-12 months", "13-24 months",
            "25-48 months", "49-72 months"]
)

with output.open("w", encoding="utf-8") as f:
    f.write("CUSTOMER CHURN & RETENTION ANALYTICS\n")
    f.write("=" * 50 + "\n\n")

    f.write(f"Total customers: {len(df)}\n")
    f.write(f"Churned customers: {(df['Churn'] == 'Yes').sum()}\n")
    f.write(f"Overall churn rate: {(df['Churn'] == 'Yes').mean() * 100:.2f}%\n")

    for column in [
        "Contract", "gender", "SeniorCitizen",
        "InternetService", "PaymentMethod", "TenureGroup"
    ]:
        f.write(f"\nCHURN BY {column.upper()}\n")
        f.write("-" * 40 + "\n")
        f.write(churn_rate(column).to_string())
        f.write("\n")

    f.write("\nAVERAGE MONTHLY CHARGES BY CHURN\n")
    f.write("-" * 40 + "\n")
    f.write(df.groupby("Churn")["MonthlyCharges"].mean().round(2).to_string())

print("EDA report generated successfully!")
print("Saved to:", output)
