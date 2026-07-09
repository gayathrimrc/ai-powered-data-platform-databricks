import mlflow

from pyspark.ml.classification import GBTClassifier
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.evaluation import BinaryClassificationEvaluator

features = spark.table("gold.customer_features")

assembler = VectorAssembler(
    inputCols=[
        "avg_logins",
        "avg_session",
        "support_cases",
        "monthly_spend"
    ],
    outputCol="features"
)

dataset = assembler.transform(features)

train, test = dataset.randomSplit([0.8, 0.2])

model = GBTClassifier(
    featuresCol="features",
    labelCol="churn"
)

with mlflow.start_run():

    trained = model.fit(train)

    predictions = trained.transform(test)

    evaluator = BinaryClassificationEvaluator()

    auc = evaluator.evaluate(predictions)

    mlflow.log_metric("AUC", auc)

    mlflow.spark.log_model(
        trained,
        "customer_churn_model"
    )

print(f"AUC = {auc}")
