import mysql.connector
import os

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST', 'mysql'),
        port=os.getenv('DB_PORT', '3306'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'password'),
        database=os.getenv('DB_NAME', 'dst_data')
    )