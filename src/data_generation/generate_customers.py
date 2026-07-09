from faker import Faker
from pyspark.sql import SparkSession
import random
from datetime import datetime, timedelta

spark = SparkSession.builder.getOrCreate()
fake = Faker()

customers = []

for customer_id in range(1, 10001):

    signup = fake.date_between("-3y", "today")

    customers.append({
        "customer_id": customer_id,
        "customer_name": fake.company(),
        "industry": random.choice([
            "Retail",
            "Finance",
            "Healthcare",
            "Technology"
        ]),
        "plan": random.choice([
            "Starter",
            "Professional",
            "Enterprise"
        ]),
        "employees": random.randint(5, 2000),
        "signup_date": signup,
        "country": fake.country()
    })

df = spark.createDataFrame(customers)

df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze.customers")
