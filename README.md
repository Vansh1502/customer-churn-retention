# Customer Churn & Retention Analytics

## Project Overview

An end-to-end data analytics and machine learning project that analyzes customer churn patterns, identifies high-risk customer segments, and predicts the likelihood of customer churn.

The project combines Python, SQL, machine learning, and an interactive Streamlit dashboard to generate actionable insights that can support customer retention strategies.

## Objectives

- Analyze customer churn trends and retention patterns.
- Identify customer segments with high churn rates.
- Explore factors associated with customer churn.
- Build machine learning models to predict customer churn.
- Develop an interactive dashboard for business insights and customer-level predictions.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Database | PostgreSQL |
| Query Language | SQL |
| Machine Learning | Scikit-learn |
| Visualization | Plotly |
| Dashboard | Streamlit |
| Testing | Pytest |
| Development | VS Code, Git, GitHub |

## Dataset

**Dataset:** IBM Telco Customer Churn

The dataset contains 7,043 customer records and includes information about customer demographics, services, contract types, billing details, tenure, and churn status.

**Target variable:** `Churn`

- `Yes` - Customer churned.
- `No` - Customer retained.

The dataset was cleaned and prepared before exploratory analysis and model development.

**Data source:** [IBM Telco Customer Churn Dataset](https://github.com/IBM/telco-customer-churn-on-icp4d)

## Key Business Findings

- Overall customer churn rate: **26.54%**.
- Month-to-month contracts have the highest churn rate: **42.71%**.
- Two-year contracts have the lowest churn rate: **2.83%**.
- Customers with tenure of 0-12 months have a churn rate of **47.44%**.
- Fiber optic customers have a churn rate of **41.89%**.
- Electronic check customers have a churn rate of **45.29%**.
- Senior citizens have a churn rate of **41.68%**, compared with **23.61%** for non-senior customers.

These findings represent observed associations, not proven causes of churn.

## Machine Learning Performance

Two classification models were developed and evaluated:

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 74.02% | 75.87% |
| Precision | 50.69% | 53.10% |
| Recall | 78.61% | 77.81% |
| F1 Score | 61.64% | 63.12% |
| ROC-AUC | 0.8416 | 0.8404 |

**Selected model:** Random Forest, based on its higher accuracy and F1 score.

The model performance is based on a held-out test dataset. Prediction scores should be interpreted as estimates rather than guarantees of customer churn.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd customer-churn-retention
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL

Create a `.env` file in the project root with your local database settings:

```env
DB_HOST=127.0.0.1
DB_PORT=5432
DB_NAME=customer_churn_db
DB_USER=your_database_user
DB_PASSWORD=your_database_password
```

Do not commit `.env` or database credentials to GitHub.

### 5. Run the Streamlit dashboard

```bash
streamlit run app/streamlit_app.py
```

The dashboard will open in your browser.

## Testing

Run the automated tests using:

```bash
python -m pytest -v
```