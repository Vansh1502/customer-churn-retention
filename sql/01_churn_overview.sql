
-- Project 2: Customer Churn & Retention Analytics
-- Query 1: Overall customer overview

SELECT
    COUNT(*) AS total_customers,

    SUM(
        CASE WHEN "Churn" = 'Yes' THEN 1 ELSE 0 END
    ) AS churned_customers,

    SUM(
        CASE WHEN "Churn" = 'No' THEN 1 ELSE 0 END
    ) AS retained_customers,

    ROUND(
        100.0 * SUM(
            CASE WHEN "Churn" = 'Yes' THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS churn_rate_percentage

FROM customers;
