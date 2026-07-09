from pyspark.sql.functions import *

customers = spark.table("silver.customers")
usage = spark.table("silver.usage")

gold = (
    customers.join(
        usage,
        "customer_id"
    )
    .groupBy("customer_id")
    .agg(
        avg("login_count").alias("avg_logins"),
        avg("session_minutes").alias("avg_session"),
        max("support_tickets").alias("support_cases"),
        avg("monthly_spend").alias("monthly_spend")
    )
)

gold.write \
    .mode("overwrite") \
    .saveAsTable("gold.customer_features")
