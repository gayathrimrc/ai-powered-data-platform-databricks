import mlflow

result = mlflow.register_model(
    "runs:/<run_id>/customer_churn_model",
    "main.ml.customer_churn"
)

print(result.version)
