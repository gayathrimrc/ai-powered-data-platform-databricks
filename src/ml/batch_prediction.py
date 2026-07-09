model = mlflow.spark.load_model(
    "models:/main.ml.customer_churn/Production"
)

customers = spark.table("gold.customer_features")

predictions = model.transform(customers)

(
    predictions
    .filter("prediction == 1")
    .write
    .mode("overwrite")
    .saveAsTable("gold.high_risk_customers")
)
