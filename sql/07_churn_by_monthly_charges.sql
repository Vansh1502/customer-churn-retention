-- Project 2: Customer Churn & Retention Analytics
-- Query 7: Average monthly charges by churn status

SELECT
    "Churn" AS churn_status,

    COUNT(*) AS total_customers,

    ROUND(AVG(monthly_charges)::numeric, 2)
        AS average_monthly_charges,

    ROUND(MIN(monthly_charges)::numeric, 2)
        AS minimum_monthly_charges,

    ROUND(MAX(monthly_charges)::numeric, 2)
        AS maximum_monthly_charges

FROM customers

GROUP BY "Churn"

ORDER BY "Churn";