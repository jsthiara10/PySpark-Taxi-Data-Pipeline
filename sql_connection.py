import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY)")

#### STEPS ####

# 1. Load in the CSV file using Spark
# 2. transform the data
# 3. Write the data to new file
# 4. Write new file to MySQL


# first, let's create our destination table in MySQL

