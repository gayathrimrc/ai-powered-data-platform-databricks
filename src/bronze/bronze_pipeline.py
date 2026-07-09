from pyspark.sql.functions import *

customers = spark.table("bronze.customers")

customers = customers.withColumn(
    "ingestion_time",
    current_timestamp()
)

customers.write \
    .mode("overwrite") \
    .saveAsTable("bronze.customers_raw")
