
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_PATH = (
    PROJECT_ROOT / "data" / "raw"
    / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
)

PROCESSED_PATH = (
    PROJECT_ROOT / "data" / "processed"
    / "customer_churn_cleaned.csv"
)


def clean_customer_data(df):
    df = df.copy()

    df["TotalCharges"] = (
        df["TotalCharges"].astype("string").str.strip()
    )

    blank_mask = (
        df["TotalCharges"].isna()
        | df["TotalCharges"].eq("")
    )

    df["TotalCharges_was_blank"] = blank_mask

    numeric_charges = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    invalid_mask = numeric_charges.isna() & ~blank_mask

    if invalid_mask.any():
        raise ValueError(
            "Unexpected non-numeric TotalCharges values."
        )

    zero_tenure_blank = blank_mask & df["tenure"].eq(0)

    if blank_mask.sum() != zero_tenure_blank.sum():
        raise ValueError(
            "Blank TotalCharges records must have zero tenure."
        )

    numeric_charges.loc[zero_tenure_blank] = 0

    df["TotalCharges"] = numeric_charges.astype(float)

    if not df["customerID"].is_unique:
        raise ValueError("Duplicate customer IDs found.")

    if df["TotalCharges"].isna().any():
        raise ValueError("Missing TotalCharges values found.")

    return df


def main():
    print("Loading raw customer dataset...")

    df = pd.read_csv(RAW_PATH)

    print("Original dataset shape:", df.shape)

    cleaned_df = clean_customer_data(df)

    PROCESSED_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    cleaned_df.to_csv(PROCESSED_PATH, index=False)

    print("\nCleaning completed successfully!")
    print("Cleaned dataset shape:", cleaned_df.shape)
    print(
        "Blank TotalCharges handled:",
        int(cleaned_df["TotalCharges_was_blank"].sum())
    )
    print("Output saved to:", PROCESSED_PATH)


if __name__ == "__main__":
    main()
