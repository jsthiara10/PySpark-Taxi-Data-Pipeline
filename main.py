from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.functions import col, trim, round
import os

# add mySQL environment variables

username = os.environ["MYSQL_USER"]
password = os.environ["MYSQL_PASS"]

# Add JBBC URL and table name

jdbc_url = "jdbc:mysql://localhost:3306/yellow_taxi_database"
table_name = "yellow_taxi_trips_jan_25"

# Parquet file environment variables

RAW_DIR = "data/raw"
CLEAN_DIR = "data/clean"
RAW_FILE = os.path.join(RAW_DIR, "nyc_taxi_data_2025-01.parquet")
CLEAN_FILE = os.path.join(CLEAN_DIR, "CLEAN_nyc_taxi_data_2025-01.parquet")

# Ensure that the directory exists

os.makedirs(CLEAN_DIR, exist_ok=True)


### EXTRACT ###

def pipeline():
    spark = SparkSession.builder \
        .appName("PySpark_Taxi_NYC") \
        .config("spark.jars", "/Users/jsthiara/Desktop/mysql-connector-j-9.5.0/mysql-connector-j-9.5.0.jar") \
        .getOrCreate()

    df = spark.read.parquet(RAW_FILE, header=True)  # Header=True keeps original column names
    print(df.head())

    transform(df)


### TRANSFORM ###

def transform(df):
    df.show()  # Preview dataframe

    # 1. Drop rows with a Passenger count of 0

    new_df = df.filter(F.col("passenger_count") != 0)  # na.drop() only removes NULL/NAN, not ZERO

    # 2. Round necessary columns

    # Round tpep pickup_datetime to nearest minute

    new_df = new_df.withColumn(
        "tpep_pickup_datetime",
        F.date_trunc(
            "minute", F.col("tpep_pickup_datetime") + F.expr("INTERVAL 30 seconds"))
    )

    # Round tpep_dropoff_datetime to nearest minute

    new_df = new_df.withColumn(
        "tpep_dropoff_datetime",
        F.date_trunc(
            "minute", F.col("tpep_dropoff_datetime") + F.expr("INTERVAL 30 seconds"))
    )

    # Round Total Amount to 1 Decimal Place

    new_df = new_df.withColumn(
        "total_amount", round(new_df.total_amount, 1))

    # Round Tip Amount to 1 Decimal Place

    new_df = new_df.withColumn(
        "tip_amount", round(new_df.tip_amount, 1))

    # Round Fare Amount to 1 Decimal Place

    new_df = new_df.withColumn(
        "fare_amount", round(new_df.fare_amount, 1))

    # Validate changes on new df

    new_df.show(truncate=False)

    new_df.printSchema()

    # Call the load function

    load(new_df)


### LOAD ###

def load(new_df):  # Create a SINGLE Parquet file using coalesce
    new_df.coalesce(1).write.parquet(CLEAN_FILE, mode='overwrite')

    # Load into MySQL Database

    new_df = new_df.repartition(4) # Number of parallel partitions
    new_df.write \
        .format("jdbc") \
        .option("url", jdbc_url) \
        .option("dbtable", table_name) \
        .option("user", username) \
        .option("password", password) \
        .option("driver", "com.mysql.cj.jdbc.Driver") \
        .option("batchsize", 5000) \
        .mode("overwrite") \
        .save()


pipeline()
