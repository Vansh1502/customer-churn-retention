-- Project 2: Customer Churn & Retention Analytics
-- Query 6: Churn analysis by senior citizen status

SELECT
    CASE
        WHEN senior_citizen = 1 THEN 'Senior Citizen'
        ELSE 'Non-Senior Citizen'
    END AS customer_category,

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

GROUP BY senior_citizen

ORDER BY senior_citizen;