import mysql.connector
import os

from datetime import datetime


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST', 'mysql'),
        port=os.getenv('DB_PORT', '3306'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'password'),
        database=os.getenv('DB_NAME', 'dst_data')
    )

def insert_dst(cursor, data):
    for entry in data[1:]:
        try:
            time_str = entry[0]
            value = float(entry[1])
            
            # Convert time string to a datetime object
            time_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            
            # Insert the data into the MySQL table
            cursor.execute("""
            INSERT INTO kyoto_dst (time_tag, dst)
            VALUES (%s, %s)
            """, (time_obj, value))
        except IndexError:
            print(f"Skipping entry due to missing fields: {entry}")
        except ValueError as e:
            print(f"Skipping entry due to value error: {entry} - {e}")