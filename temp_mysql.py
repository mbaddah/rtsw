import os
import requests
import json
from datetime import datetime
import mysql.connector

# Define the URL for the JSON data
url = "https://services.swpc.noaa.gov/products/kyoto-dst.json"

# Fetch the JSON data
response = requests.get(url)
data = response.json()

# Retrieve database connection details from environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# Connect to the MySQL database
db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = db.cursor()

# Create a table to store the data if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS kyoto_dst (
    id INT AUTO_INCREMENT PRIMARY KEY,
    time_tag DATETIME,
    dst FLOAT
)
""")

# Skip the header row and parse the JSON data to insert into the database
for entry in data[1:]:
    time_str = entry[0]
    value = float(entry[1])
    
    # Convert time string to a datetime object
    time_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    
    # Insert the data into the MySQL table
    cursor.execute("""
    INSERT INTO kyoto_dst (time_tag, dst)
    VALUES (%s, %s)
    """, (time_obj, value))

# Commit the transaction
db.commit()

# Close the database connection
cursor.close()
db.close()

print("Data inserted into MySQL database")