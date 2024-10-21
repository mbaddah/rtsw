from app.utils.db import get_db_connection
from app.utils.fetch_data import fetch_solar_wind_data
from datatime import datatime

def main():
    url = "https://services.swpc.noaa.gov/products/solar-wind/mag-2-hour.json"
    data = fetch_solar_wind_data(url)

    db = get_db_connection()
    cursor = db.cursor()

    # Move this to init-db.sql ?
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS solar_wind (
        id INT AUTO_INCREMENT PRIMARY KEY,
        time_tag DATETIME,
        bx_gsm FLOAT,
        by_gsm FLOAT,
        bz_gsm FLOAT,
        lon_gsm FLOAT,
        lat_gsm FLOAT,
        bt FLOAT
    )
    """)

    for entry in data[1:]:
        time_str = entry[0]
        bx_gsm = float(entry[1])
        by_gsm = float(entry[2])
        bz_gsm = float(entry[3])
        lon_gsm = float(entry[4])
        lat_gsm = float(entry[5])
        bt = float(entry[6])
        
        time_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
        
        cursor.execute("""
        INSERT INTO solar_wind (time_tag, bx_gsm, by_gsm, bz_gsm, lon_gsm, lat_gsm, bt)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (time_obj, bx_gsm, by_gsm, bz_gsm, lon_gsm, lat_gsm, bt))

    db.commit()
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()

# import os
# import requests
# import json
# from datetime import datetime
# import mysql.connector

# # Define the URL for the JSON data
# url = "https://services.swpc.noaa.gov/products/kyoto-dst.json"

# # Fetch the JSON data
# response = requests.get(url)
# data = response.json()

# # Retrieve database connection details from environment variables
# db_host = os.getenv('DB_HOST', 'mysql')
# db_port = os.getenv('DB_PORT', '3306')
# db_user = os.getenv('DB_USER', 'root')
# db_password = os.getenv('DB_PASSWORD', 'password')
# db_name = os.getenv('DB_NAME', 'dst_data')

# # Connect to the MySQL database
# db = mysql.connector.connect(
#     host=db_host,
#     port=db_port,
#     user=db_user,
#     password=db_password,
#     database=db_name
# )

# cursor = db.cursor()

# # Create a table to store the data if it doesn't exist
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS kyoto_dst (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     time_tag DATETIME,
#     dst FLOAT
# )
# """)

# # Skip the header row and parse the JSON data to insert into the database
# for entry in data[1:]:
#     time_str = entry[0]
#     value = float(entry[1])
    
#     # Convert time string to a datetime object
#     time_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    
#     # Insert the data into the MySQL table
#     cursor.execute("""
#     INSERT INTO kyoto_dst (time_tag, dst)
#     VALUES (%s, %s)
#     """, (time_obj, value))

# # Commit the transaction
# db.commit()

# # Close the database connection
# cursor.close()
# db.close()

# print("Data inserted into MySQL database")