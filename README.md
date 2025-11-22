# **PySpark to MySQL Taxi Data Project (In-Development)**

**This project transforms 3 million records for Taxi Data in New York City using PySpark, and writes them to MySQL using a scheduled cron job**

![Apache Spark Logo](images/apache-spark-logo.png)
![MySQL Logo](images/my-sql-logo.png)


# **Overview**

The purpose of this project is to mimic a production-grade Extract, Transform & Load (ETL) Pipeline which uses parallel processing to
transform and write approximately 3 million records using PySpark, to a MySQL database

Data Engineers often have to use parallel processing when transforming large datasets and utlising Apache Spark is one such way to achieve this.
Additionally, engineers may often automate large jobs to run out-of-hours schedule, to minimise strain on database capacity during peak hours.

Spark works well with Python using the PySpark library, which is used for data transformation in this pipeline. Additionally, a cron job is a simple way to
schedule data pipelines that have few or no dependencies on other ETL jobs - such as this pipeline.

This project transforms a large dataset containing around 3 million records for Yellow Taxi Data in New York City, for the month of January 2025.

# Architecture 

![pyspark-diagram-1](images/pyspark-diagram-1.png)

The PySpark job will run on a cron scheduler, which can be scheduled for the time most appropriate for the user.

The ingestion layer comprises of 3 million records related to Yellow Taxi data in New York City contained in a Parquet file.

At the transformation layer, data cleansing will occur via PySpark which will normalise data, perform rounding of numerical values, drop nulls and much more - you are also free to add your own transformations to the source code if you so wish.

As per the user-defined cron schedule time, the PySpark transformations will take place automatically and then write them to a MySQL database. 
At the analytics layer, there will be clean data ready for Business Intelligence, Machine Learning and reporting use-cases.

# Technologies Used:

**PySpark**

**MySQL 9.5**

**Python 3.9** (to use with Spark)

**Java 17** (to use with Spark)

**Linux** (for cron job) - **Alternatively for Windows, you can use Task Scheduler**


# **Set Up:**

## **Part 1 - MySQL**

**Download MySQL Community Server 9.5.0 for your respective OS here:**

https://dev.mysql.com/downloads/mysql/

**Download MySQL Connector/J 9.5.0 (so Spark can connect to MySQL)**

https://dev.mysql.com/downloads/connector/j/

Once downloaded, go through the instructions and set up your ROOT user

You can also create a separate user if you so desire, but for the purposes of this project we'll be using Root

Once Root User and Password are set up, please add the following to your PATH variables 

* MySQL Version
* MySQL Root User
* MySQL Root Password

This process will vary depending on your OS system but this will allow us to use relative paths and avoid hard-coding credentials

## **Part 2 - Spark, Python, Java**

**Spark requires you to have a supported Java version installed (8, 11, 17 - version 17 has been used for this project)**

You can download the appropriate Java version here: https://www.java.com/en/

**We will also be using Python 3.9 in order for PySpark to work**

Please download Python 3.9 here: https://www.python.org/downloads/

**Please consult the following links to download Spark/setup Spark on your personal machine**

https://spark.apache.org/downloads.html

**Windows Set Up:** https://www.youtube.com/watch?v=JjIwAMXUvYc

**Mac Set Up:** https://www.youtube.com/watch?v=OGHyEXrvkF0

## Part 3 - Repo & Virtual Environment  ##

**1. Clone and/or fork this repository**

````
git clone https://github.com/jsthiara10/PySpark-Taxi-Data-Pipeline.git
````

**2. Setup a virtual environment, using **Python 3.9 (Important)****

To avoid dependency conflict, we'll be using a Virtual Environment

Open your IDE of choice and navigate to the project directory

Give your virtual environment an appropriate name, such as venv or spark39

````
python3.9 -m venv spark39
````

**Activate your virtual environment**

````
source spark39/bin/activate
````

**To deactivate your virtual environment, simply enter the following command**

````
deactivate
````

**4. Set up your data folders**

We'll be using relative paths for our Extract and Load processes

Still in your virtual environment, create the following folder

````
mkdir data
````

Switch to your data directory 

````
cd data
````

Then in the data folder, create the following directories

Our raw folder will contain the source Parquet file, whilst our clean folder will have a cleaned version of our Parquet file
written to it at the end of the ETL process

````
mkdir raw

mkdir clean
````


Switch back to your project directory

````
cd [your-project-directory]
````

**5. Drop the raw file into the raw folder**

Using the following link, **download the Parquet file** we will perform our ETL process on

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page 

Scroll down and click on the link for **Yellow Taxi Trip Records for January 2025**, to download the Parquet file

![Parquet file](images/taxi-download.png)

Once you've downloaded the file, **drag & drop to the raw folder** (alternatively, download directly to raw folder)

# **Configure Cron Job**

TBC



