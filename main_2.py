from pyspark.sql import SparkSession
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

    df = spark.read.csv(RAW_FILE)

    print(df.head())

    transform(df)


### TRANSFORM ###

def transform(df):
    print(df.count())

    # Drop Null Values

    df.na.drop().show()

    # Drop any rows that have reviews before January 2009




main()
