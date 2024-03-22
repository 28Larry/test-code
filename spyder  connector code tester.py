import mysql.connector

# Establish connection with MySQL server
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="deny"
        )
        print("Connected to MySQL server successfully!")
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to MySQL server:", error)

# Create a new database
def create_database(connection, database_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' created successfully!")
    except mysql.connector.Error as error:
        print("Error creating database:", error)
    finally:
        if connection.is_connected():
            cursor.close()

# Example usage
if __name__ == "__main__":
    connection = connect_to_mysql()
    if connection:
        create_database(connection, "PowerSellerDB")
        connection.close()
        

