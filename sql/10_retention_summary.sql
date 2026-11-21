-- Project 2: Customer Churn & Retention Analytics
-- Query 10: Overall customer retention summary

SELECT
    COUNT(*) AS total_customers,

    COUNT(*) FILTER (
        WHERE "Churn" = 'Yes'
    ) AS churned_customers,

    COUNT(*) FILTER (
        WHERE "Churn" = 'No'
    ) AS retained_customers,

    ROUND(
        100.0 * COUNT(*) FILTER (
            WHERE "Churn" = 'Yes'
        ) / COUNT(*),
        2
    ) AS churn_rate_percentage,

    ROUND(
        AVG(monthly_charges)::numeric,
        2
    ) AS average_monthly_charges,

    ROUND(
        SUM(monthly_charges) FILTER (
            WHERE "Churn" = 'Yes'
        )::numeric,
        2
    ) AS monthly_charges_associated_with_churn

FROM customers;