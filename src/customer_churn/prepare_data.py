import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "customer_churn_features.csv"
)


def prepare_data():

    print("Loading feature dataset...")

    df = pd.read_csv(INPUT_PATH)

    # Separate input features and target variable
    X = df.drop(columns=["Churn"])
    y = df["Churn"]

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("\nData preparation completed!")

    print("Training features:", X_train.shape)
    print("Testing features:", X_test.shape)

    print("\nTraining churn distribution:")
    print(y_train.value_counts(normalize=True).round(3))

    print("\nTesting churn distribution:")
    print(y_test.value_counts(normalize=True).round(3))


if __name__ == "__main__":
    prepare_data()