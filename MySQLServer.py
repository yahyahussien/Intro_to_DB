import mysql.connector
from mysql.connector import errorcode

# Database connection configuration
config = {
    'user': 'Allano', 
    'password': '@Allanoss123',  
    'host': 'localhost',  # Or your MySQL server host
}

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")

def main():
    try:
        # Connect to MySQL server
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # Create the database
        create_database(cursor)

    except mysql.connector.Error as err:
        # Handle errors when connecting to MySQL server
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid credentials, please check your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"Error: {err}")
    finally:
        # Ensure the cursor and connection are closed
        if 'cursor' in locals():
            cursor.close()
        if 'cnx' in locals():
            cnx.close()

if __name__ == "__main__":
    main()
