
import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "customer_churn_features.csv"
)


def train_random_forest():

    print("Loading feature dataset...")

    df = pd.read_csv(INPUT_PATH)

    # Separate features and target
    X = df.drop(columns=["Churn"])
    y = df["Churn"]

    # Use the same split as Logistic Regression
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    # Create Random Forest model
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        class_weight="balanced",
        random_state=42,
        n_jobs=-1
    )

    print("\nTraining Random Forest model...")

    model.fit(X_train, y_train)

    # Generate predictions
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # Evaluate model
    accuracy = accuracy_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_prob)

    print("\nRandom Forest training completed!")

    print("\nAccuracy:", round(accuracy * 100, 2), "%")
    print("ROC-AUC:", round(roc_auc, 4))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))


if __name__ == "__main__":
    train_random_forest()
