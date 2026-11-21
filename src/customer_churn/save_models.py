
import pandas as pd
import joblib

from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = PROJECT_ROOT / "data" / "processed" / "customer_churn_features.csv"
MODEL_DIR = PROJECT_ROOT / "models"


def save_models():

    df = pd.read_csv(DATA_PATH)

    X = df.drop(columns=["Churn"])
    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    models = {
        "logistic_regression": Pipeline([
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
                random_state=42
            ))
        ]),

        "random_forest": RandomForestClassifier(
            n_estimators=200,
            max_depth=10,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1
        )
    }

    results = []

    for name, model in models.items():

        print(f"\nTraining {name}...")

        model.fit(X_train, y_train)

        predictions = model.predict(X_test)
        probabilities = model.predict_proba(X_test)[:, 1]

        results.append({
            "Model": name,
            "Accuracy": accuracy_score(y_test, predictions),
            "Precision": precision_score(y_test, predictions),
            "Recall": recall_score(y_test, predictions),
            "F1_Score": f1_score(y_test, predictions),
            "ROC_AUC": roc_auc_score(y_test, probabilities)
        })

        model_path = MODEL_DIR / f"{name}.joblib"

        joblib.dump(model, model_path)

        print("Saved:", model_path)

    results_df = pd.DataFrame(results)

    results_df.to_csv(
        PROJECT_ROOT / "reports" / "model_comparison.csv",
        index=False
    )

    print("\nModel comparison:")
    print(results_df.round(4).to_string(index=False))

    print("\nBoth models saved successfully!")


if __name__ == "__main__":
    save_models()
