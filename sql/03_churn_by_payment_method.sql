-- Project 2: Customer Churn & Retention Analytics
-- Query 3: Churn analysis by payment method

SELECT
    "PaymentMethod" AS payment_method,

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

GROUP BY "PaymentMethod"

ORDER BY churn_rate_percentage DESC;