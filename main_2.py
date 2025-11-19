from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim
import os

RAW_DIR = "data/raw"
CLEAN_DIR = "data/clean"
RAW_FILE = os.path.join(RAW_DIR, "airbnb_raw.csv")
CLEAN_FILE = os.path.join(CLEAN_DIR, "airbnb_clean.csv")

# Ensure that the directory exists

os.makedirs(CLEAN_DIR, exist_ok=True)


### EXTRACT ###

def main():
    spark = SparkSession.builder \
        .appName("CSV_Transformation") \
        .getOrCreate()

    df = spark.read.csv(RAW_FILE, header=True)  # Header=True keeps original column names
    print(df.head())

    transform(df)


### TRANSFORM ###

def transform(df):
    print(df.count())

    df.show()  # Preview dataframe

    # Drop Null Values

    new_df = df.na.drop()  # all nulls removed

    # Drop rows where room_type is Entire home/apt

    new_df = new_df.where(col("room_type") != "Entire home/apt")

    # String transformations

    # Remove whitespace

    new_df = df.withColumn("name", trim(col("name")))

    new_df.show(truncate=False)

    load(new_df)


### LOAD ###

def load(new_df):
    new_df.write.csv(CLEAN_FILE, header=True, mode='overwrite')


main()
