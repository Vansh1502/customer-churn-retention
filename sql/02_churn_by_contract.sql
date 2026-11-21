
-- Project 2: Customer Churn & Retention Analytics
-- Query 2: Churn analysis by contract type

SELECT
    "Contract" AS contract_type,

    COUNT(*) AS total_customers,

    SUM(
        CASE WHEN "Churn" = 'Yes' THEN 1 ELSE 0 END
    ) AS churned_customers,

    ROUND(
        100.0 * SUM(
            CASE WHEN "Churn" = 'Yes' THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS churn_rate_percentage

FROM customers

GROUP BY "Contract"

ORDER BY churn_rate_percentage DESC;
