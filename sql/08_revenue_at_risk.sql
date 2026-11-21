-- Project 2: Customer Churn & Retention Analytics
-- Query 8: Monthly revenue associated with churned customers

SELECT
    COUNT(*) AS churned_customers,

    ROUND(
        SUM(monthly_charges)::numeric,
        2
    ) AS monthly_revenue_at_risk,

    ROUND(
        AVG(monthly_charges)::numeric,
        2
    ) AS average_monthly_charge

FROM customers

WHERE "Churn" = 'Yes';