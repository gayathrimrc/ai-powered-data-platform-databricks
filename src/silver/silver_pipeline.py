from pyspark.sql.functions import *

bronze = spark.table("bronze.customers_raw")

silver = (
    bronze
    .dropDuplicates(["customer_id"])
    .filter(col("customer_name").isNotNull())
    .filter(col("plan").isNotNull())
)

silver.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("silver.customers")
