import logging
import utils.db_config as db_config
import utils.kyoto_dst_request as kyoto_dst_request

logging.basicConfig(level=logging.INFO)

def main():
    # Fetch the data
    data = kyoto_dst_request.fetch_kyoto_dst()
    
    # Connect to the MySQL database
    db = db_config.get_db_connection()
    cursor = db.cursor()
    
    db_config.insert_dst(cursor, data)

    # Commit the transaction
    db.commit()

    # Close the database connection
    cursor.close()
    db.close()

    logging.info("Sucessfully inserted data into the database")


if __name__ == "__main__":
    main()