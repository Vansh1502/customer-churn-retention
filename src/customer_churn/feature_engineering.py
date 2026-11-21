
import pandas as pd
from pathlib import Path

# Project directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Dataset paths
INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "customer_churn_cleaned.csv"
)

OUTPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "customer_churn_features.csv"
)


def create_features():
    print("Loading cleaned customer dataset...")

    df = pd.read_csv(INPUT_PATH)

    # Remove customer ID because it does not help predict churn
    df = df.drop(columns=["customerID"])

    # Convert target variable into numerical values
    df["Churn"] = df["Churn"].map({
        "No": 0,
        "Yes": 1
    })

    # Convert categorical variables into numerical columns
    df = pd.get_dummies(
        df,
        drop_first=True,
        dtype=int
    )

    print("Feature engineering completed!")
    print("Final dataset shape:", df.shape)

    # Save processed features
    df.to_csv(OUTPUT_PATH, index=False)

    print("Feature dataset saved to:", OUTPUT_PATH)


if __name__ == "__main__":
    create_features()
