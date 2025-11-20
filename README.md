# **PySpark Taxi Data Project (In-Development)**

**This project transforms 3 million records for Taxi Data in New York City using PySpark**

![Apache Spark Logo](images/apache-spark-logo.png)

**Technologies Used:**

**PySpark**

**Python 3.9**


##  **Instructions**

**1. Clone (and optionally, fork) this repository**

**2. Install the requirements - you will need to download Spark separately for your respective OS.**

**Please consult the following links to download Spark/setup Spark on your personal machine**

https://spark.apache.org/downloads.html

**Windows Set Up:** https://www.youtube.com/watch?v=JjIwAMXUvYc

**Mac Set Up:** https://www.youtube.com/watch?v=OGHyEXrvkF0

**3. Setup a virtual environment, using **Python 3.9 (Important)****

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

In your project directory, create the following folder

````
mkdir data
````

Switch to your data directory 

````
cd data
````

Then in the data folder, create the following directories

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

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page (UPDATE with pictures)

Once you've downloaded the file, **drag & drop to the raw folder** (alternatively, download directly to raw folder)

