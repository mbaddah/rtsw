from datetime import datetime
import utils.db_config as db_config
import utils.kyoto_dst_request as kyoto_dst_request

def main():
    # Fetch the data
    data = kyoto_dst_request.request_kyoto_dst()
    print(data)
    
    # Connect to the MySQL database
    db = db_config.get_db_connection()
    cursor = db.cursor()

    # Skip the header row and parse the JSON data to insert into the database
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
        except IndexError as e:
            print(f"Skipping entry due to missing fields: {entry}")
        except ValueError as e:
            print(f"Skipping entry due to value error: {entry} - {e}")

    # Commit the transaction
    db.commit()

    # Close the database connection
    cursor.close()
    db.close()

    print("Data inserted into MySQL database")

if __name__ == "__main__":
    main()