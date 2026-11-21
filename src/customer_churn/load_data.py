
import pandas as pd
from pathlib import Path
from sqlalchemy import text

from src.customer_churn.db import engine

# Define the cleaned dataset path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "customer_churn_cleaned.csv"

def load_customer_data():
    print("Reading cleaned customer dataset...")

    df = pd.read_csv(DATA_PATH)

    print("Dataset shape:", df.shape)

    # Rename columns to PostgreSQL-friendly names
    df = df.rename(columns={
        "customerID": "customer_id",
        "SeniorCitizen": "senior_citizen",
        "TotalCharges": "total_charges",
        "MonthlyCharges": "monthly_charges",
        "TotalCharges_was_blank": "total_charges_was_blank"
    })

    print("Loading records into PostgreSQL...")

    # Import data into the customers table
    df.to_sql(
        name="customers",
        con=engine,
        if_exists="replace",
        index=False,
        method="multi",
        chunksize=500
    )

    print("Data loaded successfully!")

    # Verify imported records
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT COUNT(*) FROM customers")
        )
        count = result.scalar()

    print("Total records in PostgreSQL:", count)


if __name__ == "__main__":
    load_customer_data()
