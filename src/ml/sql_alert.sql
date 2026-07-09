SELECT
    COUNT(*) /
    (SELECT COUNT(*) FROM gold.customer_predictions)
AS churn_rate
FROM gold.customer_predictions
WHERE prediction = 1;

---Configure a Databricks SQL Alert to trigger when:

--churn_rate > 0.35
