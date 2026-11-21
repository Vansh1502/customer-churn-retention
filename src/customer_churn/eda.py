import pandas as pd

DATA_PATH = "data/processed/customer_churn_cleaned.csv"

df = pd.read_csv(DATA_PATH)

print("=" * 50)
print("CUSTOMER CHURN ANALYSIS")
print("=" * 50)

# 1. Dataset overview
print("\n1. DATASET OVERVIEW")
print("Total customers:", len(df))
print("Total columns:", len(df.columns))

# 2. Churn summary
print("\n2. CHURN DISTRIBUTION")
print(df["Churn"].value_counts())

print("\nChurn percentage:")
print((df["Churn"].value_counts(normalize=True) * 100).round(2))

# 3. Customer demographics
print("\n3. GENDER DISTRIBUTION")
print(df["gender"].value_counts())

print("\n4. SENIOR CITIZEN DISTRIBUTION")
print(df["SeniorCitizen"].value_counts())

# 4. Contract distribution
print("\n5. CONTRACT DISTRIBUTION")
print(df["Contract"].value_counts())

# 5. Tenure summary
print("\n6. CUSTOMER TENURE SUMMARY")
print(df["tenure"].describe().round(2))

# 6. Monthly charges summary
print("\n7. MONTHLY CHARGES SUMMARY")
print(df["MonthlyCharges"].describe().round(2))

# 7. Average charges by churn status
print("\n8. AVERAGE MONTHLY CHARGES BY CHURN")
print(df.groupby("Churn")["MonthlyCharges"].mean().round(2))

print("\nEDA summary completed successfully!")
