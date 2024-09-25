import mysql.connector

def create_database(database_name):
    """Creates a new database in MySQL.

    Args:
        database_name: The name of the database to create.
    """

    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Irfan1234"
        )

        cursor = cnx.cursor()

        # Create the database
        cursor.execute(f"CREATE DATABASE {database_name}")

        print(f"Database '{database_name}' created successfully.")

    except mysql.connector.Error as err:
        print(f"Error creating database: {err}")
    finally:
        cursor.close()
        cnx.close()
        