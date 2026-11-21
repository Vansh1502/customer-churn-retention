
import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "customer_churn_features.csv"
)


def analyze_feature_importance():

    print("Loading feature dataset...")

    df = pd.read_csv(INPUT_PATH)

    X = df.drop(columns=["Churn"])
    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        class_weight="balanced",
        random_state=42,
        n_jobs=-1
    )

    print("\nTraining Random Forest model...")

    model.fit(X_train, y_train)

    # Extract feature importance
    importance_df = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    print("\nTop 10 Churn Prediction Features:")

    print(
        importance_df.head(10).to_string(index=False)
    )

    # Save complete feature importance report
    output_path = (
        PROJECT_ROOT
        / "reports"
        / "feature_importance.csv"
    )

    importance_df.to_csv(output_path, index=False)

    print("\nFeature importance report saved to:")
    print(output_path)


if __name__ == "__main__":
    analyze_feature_importance()
