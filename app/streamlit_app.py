
import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "customer_churn_cleaned.csv"
)

MODEL_DIR = PROJECT_ROOT / "models"

# Page configuration
st.set_page_config(
    page_title="Customer Churn & Retention Analytics",
    page_icon="📊",
    layout="wide"
)

# Dashboard heading
st.title("Customer Churn & Retention Analytics")

st.markdown(
    "Analyze customer behavior, understand churn patterns, "
    "and identify opportunities to improve retention."
)

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()
# Create numerical churn indicator for all analyses
df["ChurnFlag"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

# Calculate business metrics
total_customers = len(df)

churned_customers = (df["Churn"] == "Yes").sum()

retained_customers = (df["Churn"] == "No").sum()

churn_rate = (
    churned_customers / total_customers
) * 100

average_monthly_charges = df["MonthlyCharges"].mean()

# KPI section
st.subheader("Business Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Customers",
    f"{total_customers:,}"
)

col2.metric(
    "Churned Customers",
    f"{churned_customers:,}"
)

col3.metric(
    "Churn Rate",
    f"{churn_rate:.2f}%"
)

col4.metric(
    "Average Monthly Charges",
    f"${average_monthly_charges:.2f}"
)

st.divider()

# Churn distribution
st.subheader("Customer Churn Distribution")

churn_counts = (
    df["Churn"]
    .value_counts()
    .reset_index()
)

churn_counts.columns = ["Churn Status", "Customers"]

fig = px.pie(
    churn_counts,
    names="Churn Status",
    values="Customers",
    title="Retained vs Churned Customers",
    hole=0.45
)

st.plotly_chart(fig, use_container_width=True)


# Churn Rate by Payment Method

st.subheader("Churn Rate by Payment Method")

payment_churn = (
    df.groupby("PaymentMethod")["ChurnFlag"]
    .mean()
    .mul(100)
    .reset_index(name="Churn Rate")
    .sort_values("Churn Rate", ascending=False)
)

fig_payment = px.bar(
    payment_churn,
    x="PaymentMethod",
    y="Churn Rate",
    text_auto=".2f",
    title="Customer Churn Rate by Payment Method",
    labels={
        "PaymentMethod": "Payment Method",
        "Churn Rate": "Churn Rate (%)"
    }
)

fig_payment.update_layout(
    yaxis_range=[0, 55],
    xaxis_tickangle=-20
)

st.plotly_chart(
    fig_payment,
    use_container_width=True
)


# Churn Rate by Internet Service

st.subheader("Churn Rate by Internet Service")

internet_churn = (
    df.groupby("InternetService")["ChurnFlag"]
    .mean()
    .mul(100)
    .reset_index(name="Churn Rate")
    .sort_values("Churn Rate", ascending=False)
)

fig_internet = px.bar(
    internet_churn,
    x="InternetService",
    y="Churn Rate",
    text_auto=".2f",
    title="Customer Churn Rate by Internet Service",
    labels={
        "InternetService": "Internet Service",
        "Churn Rate": "Churn Rate (%)"
    }
)

fig_internet.update_layout(
    yaxis_range=[0, 50]
)

st.plotly_chart(
    fig_internet,
    use_container_width=True
)


# Machine Learning Model Performance

st.divider()

st.header("Machine Learning Model Performance")

# Load model comparison report
comparison_path = (
    PROJECT_ROOT / "reports" / "model_comparison.csv"
)

model_results = pd.read_csv(comparison_path)

st.subheader("Model Comparison")

# Display model performance table
st.dataframe(
    model_results,
    use_container_width=True,
    hide_index=True
)

# Compare evaluation metrics
metrics = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1_Score",
    "ROC_AUC"
]

comparison_long = model_results.melt(
    id_vars="Model",
    value_vars=metrics,
    var_name="Metric",
    value_name="Score"
)

fig_models = px.bar(
    comparison_long,
    x="Metric",
    y="Score",
    color="Model",
    barmode="group",
    title="Logistic Regression vs Random Forest",
    labels={
        "Score": "Performance Score",
        "Metric": "Evaluation Metric"
    },
    text_auto=".2f"
)

fig_models.update_layout(
    yaxis_range=[0, 1]
)

st.plotly_chart(
    fig_models,
    use_container_width=True
)

# Individual Customer Churn Prediction

st.divider()

st.header("Customer Churn Prediction")

st.write(
    "Enter customer details below to estimate "
    "their likelihood of leaving the service."
)

with st.form("churn_prediction_form"):

    st.subheader("Customer Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        senior = st.selectbox("Senior Citizen", [0, 1])
        partner = st.selectbox("Has Partner", ["Yes", "No"])
        dependents = st.selectbox("Has Dependents", ["Yes", "No"])
        tenure = st.slider("Tenure (months)", 0, 72, 12)
        phone = st.selectbox("Phone Service", ["Yes", "No"])

    with col2:
        multiple_lines = st.selectbox(
            "Multiple Lines",
            ["No", "Yes", "No phone service"]
        )
        internet = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )
        security = st.selectbox(
            "Online Security",
            ["Yes", "No", "No internet service"]
        )
        backup = st.selectbox(
            "Online Backup",
            ["Yes", "No", "No internet service"]
        )
        protection = st.selectbox(
            "Device Protection",
            ["Yes", "No", "No internet service"]
        )
        support = st.selectbox(
            "Tech Support",
            ["Yes", "No", "No internet service"]
        )

    with col3:
        streaming_tv = st.selectbox(
            "Streaming TV",
            ["Yes", "No", "No internet service"]
        )
        streaming_movies = st.selectbox(
            "Streaming Movies",
            ["Yes", "No", "No internet service"]
        )
        contract = st.selectbox(
            "Contract",
            ["Month-to-month", "One year", "Two year"]
        )
        paperless = st.selectbox(
            "Paperless Billing", ["Yes", "No"]
        )
        payment = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

    st.subheader("Billing Information")

    col4, col5 = st.columns(2)

    with col4:
        monthly_charges = st.number_input(
            "Monthly Charges ($)",
            min_value=0.0,
            max_value=200.0,
            value=70.0
        )

    with col5:
        total_charges = st.number_input(
            "Total Charges ($)",
            min_value=0.0,
            max_value=20000.0,
            value=840.0
        )

    selected_model = st.selectbox(
        "Select Prediction Model",
        ["random_forest", "logistic_regression"]
    )

    submitted = st.form_submit_button(
        "Predict Customer Churn"
    )

if submitted:

    customer = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple_lines,
        "InternetService": internet,
        "OnlineSecurity": security,
        "OnlineBackup": backup,
        "DeviceProtection": protection,
        "TechSupport": support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        "TotalCharges_was_blank": 0
    }])

    # Apply the same encoding used during model training
    customer_encoded = pd.get_dummies(
        customer,
        drop_first=True,
        dtype=int
    )

        # Load selected model
    model = joblib.load(
        MODEL_DIR / f"{selected_model}.joblib"
    )

    # Match the exact training feature columns and order
    customer_encoded = customer_encoded.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )

    prediction = model.predict(customer_encoded)[0]

    probability = model.predict_proba(
        customer_encoded
    )[0][1]

    st.subheader("Prediction Result")

    st.metric(
        "Estimated Churn Probability",
        f"{probability:.2%}"
    )

    if probability >= 0.50:
        st.error("High Churn Risk: This customer has a high likelihood of leaving.")

    elif probability >= 0.30:
        st.warning("Medium Churn Risk: This customer may need retention attention.")

    else:
        st.success("Low Churn Risk: This customer has a relatively low likelihood of leaving.")

# Customer data preview
st.subheader("Customer Data Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)


# Churn Rate by Customer Tenure
# Convert churn labels into numerical values
df["ChurnFlag"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})
st.subheader("Churn Rate by Customer Tenure")

# Create tenure groups
df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, 72],
    labels=[
        "0-12 Months",
        "13-24 Months",
        "25-48 Months",
        "49-72 Months"
    ]
)

tenure_churn = (
    df.groupby("TenureGroup", observed=False)["ChurnFlag"]
    .mean()
    .mul(100)
    .reset_index(name="Churn Rate")
)

fig_tenure = px.bar(
    tenure_churn,
    x="TenureGroup",
    y="Churn Rate",
    text_auto=".2f",
    title="Customer Churn Rate by Tenure",
    labels={
        "TenureGroup": "Customer Tenure",
        "Churn Rate": "Churn Rate (%)"
    }
)

fig_tenure.update_layout(
    yaxis_range=[0, 55]
)

st.plotly_chart(
    fig_tenure,
    use_container_width=True
)


# Churn Analysis
st.divider()

st.header("Customer Churn Analysis")

st.subheader("Churn Rate by Contract Type")

# Convert churn labels into numerical values
df["ChurnFlag"] = df["Churn"].map({
    "No": 0,
    "Yes": 1
})

# Calculate churn rate by contract
contract_churn = (
    df.groupby("Contract")["ChurnFlag"]
    .mean()
    .mul(100)
    .reset_index(name="Churn Rate")
)

# Create bar chart
fig_contract = px.bar(
    contract_churn,
    x="Contract",
    y="Churn Rate",
    text_auto=".2f",
    title="Customer Churn Rate by Contract Type",
    labels={
        "Contract": "Contract Type",
        "Churn Rate": "Churn Rate (%)"
    }
)

fig_contract.update_layout(
    yaxis_range=[0, 50]
)

st.plotly_chart(
    fig_contract,
    use_container_width=True
)
