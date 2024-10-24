import requests
from datetime import datetime
import utils.db_config as db_config

# Define the URL for the JSON data
url = "https://services.swpc.noaa.gov/products/kyoto-dst.json"

# Fetch the JSON data
response = requests.get(url)
data = response.json()

# Connect to the MySQL database
db = db_config.get_db_connection()

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