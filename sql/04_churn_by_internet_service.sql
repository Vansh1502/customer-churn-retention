-- Project 2: Customer Churn & Retention Analytics
-- Query 4: Churn analysis by internet service

SELECT
    "InternetService" AS internet_service,

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

GROUP BY "InternetService"

ORDER BY churn_rate_percentage DESC;