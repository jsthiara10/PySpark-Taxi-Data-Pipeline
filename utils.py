# Environment variables for pipeline
import os
# MySQL environment variables

username = os.environ["MYSQL_USER"]
password = os.environ["MYSQL_PASS"]

# JBBC URL and table name

jdbc_url = "jdbc:mysql://localhost:3306/yellow_taxi_database"
table_name = "yellow_taxi_trips_jan_25"

# Parquet file environment variables

RAW_DIR = "data/raw"
CLEAN_DIR = "data/clean"
RAW_FILE = os.path.join(RAW_DIR, "nyc_taxi_data_2025-01.parquet")
CLEAN_FILE = os.path.join(CLEAN_DIR, "CLEAN_nyc_taxi_data_2025-01.parquet")

