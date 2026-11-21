-- Project 2: Customer Churn & Retention Analytics
-- Query 9: Customer segmentation by tenure

SELECT
    CASE
        WHEN tenure <= 12 THEN 'New Customers'
        WHEN tenure <= 24 THEN 'Growing Customers'
        ELSE 'Established Customers'
    END AS customer_segment,

    COUNT(*) AS total_customers,

    SUM(
        CASE WHEN "Churn" = 'Yes' THEN 1 ELSE 0 END
    ) AS churned_customers,

    ROUND(
        100.0 * SUM(
            CASE WHEN "Churn" = 'Yes' THEN 1 ELSE 0 END
        ) / COUNT(*),
        2
    ) AS churn_rate_percentage,

    ROUND(
        AVG(monthly_charges)::numeric,
        2
    ) AS average_monthly_charges

FROM customers

GROUP BY 1

ORDER BY MIN(tenure);