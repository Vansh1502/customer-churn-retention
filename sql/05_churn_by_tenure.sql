-- Project 2: Customer Churn & Retention Analytics
-- Query 5: Churn analysis by tenure group

SELECT
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49-72 Months'
    END AS tenure_group,

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

GROUP BY
    CASE
        WHEN tenure <= 12 THEN 1
        WHEN tenure <= 24 THEN 2
        WHEN tenure <= 48 THEN 3
        ELSE 4
    END,
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49-72 Months'
    END

ORDER BY MIN(tenure);