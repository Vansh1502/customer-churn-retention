import pandas as pd

DATA_PATH = "data/processed/customer_churn_cleaned.csv"
df = pd.read_csv(DATA_PATH)

def churn_analysis(column):
    print("\n" + "=" * 55)
    print(f"CHURN RATE BY {column.upper()}")
    print("=" * 55)

    result = (
        df.groupby(column, observed=True)["Churn"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .round(2)
        .sort_values(ascending=False)
    )

    print(result.to_string())

churn_analysis("Contract")
churn_analysis("gender")
churn_analysis("SeniorCitizen")
churn_analysis("InternetService")
churn_analysis("PaymentMethod")

print("\nSegment analysis completed successfully!")
