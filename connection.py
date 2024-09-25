import mysql.connector
import bcrypt

'''.......................................................'''
def create_user_table():

    try:
        with mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Irfan1234",
            database="my_database"
        ) as mydb:

            with mydb.cursor() as mycursor:
                query = """
                CREATE TABLE owner (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    email VARCHAR(255),
                    # Add other profile fields as needed
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
                mycursor.execute(query)

                return True

    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
        return False

'''..................................................'''


def create_user(username, password, email):
    """Creates a new user account."""
    try:
        with mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Irfan1234",
            database="my_database"
        ) as mydb:
            with mydb.cursor() as mycursor:
                hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                sql = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
                mycursor.execute(sql, (username, hashed_password, email))
                mydb.commit()
                return True
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
'''........................................................'''

def login_user(username, password):
    """Authenticates a user."""
    try:
        with mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Irfan1234",
            database="my_database"
        ) as mydb:
            with mydb.cursor() as mycursor:
                sql = "SELECT password FROM users WHERE username = %s"
                mycursor.execute(sql, (username,))
                result = mycursor.fetchone()
                if result and bcrypt.checkpw(password.encode(), result[0].encode()):
                    return True
                else:
                    return False
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    
    
def login_owner(username, password):
    """Authenticates a user."""
    try:
        with mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Irfan1234",
            database="my_database"
        ) as mydb:
            with mydb.cursor() as mycursor:
                sql = "SELECT password FROM owner WHERE username = %s"
                mycursor.execute(sql, (username,))
                result = mycursor.fetchone()
                if result and bcrypt.checkpw(password.encode(), result[0].encode()):
                    return True
                else:
                    return False
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False    



    
    


'''.......................................................'''

def create_table(table_name, column_definitions):
    mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Irfan1234",
    database="my_database"
)
    with mydb.cursor() as mycursor:
        column_defs = ", ".join(f"{col} {data_type}" for col, data_type in column_definitions)
        query = f"CREATE TABLE {table_name} ({column_defs})"
        mycursor.execute(query)
        return mycursor.rowcount

def insert_data(data):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Irfan1234",
            database="my_database"
        )
        cursor = mydb.cursor()

        sql = "INSERT INTO income (amount, created_date) VALUES (%s, %s)"
        cursor.executemany(sql, data)

        mydb.commit()
        print("Data inserted successfully.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        mydb.close()
    
def display_data(table):
    mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Irfan1234",
    database="my_database"
) 
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)



def fetch_data_by_date_range(start_date, end_date):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Irfan1234",
            database="my_database"
        )

        cursor = mydb.cursor()

        query = "SELECT * FROM income WHERE created_date BETWEEN %s AND %s"
        cursor.execute(query, (start_date, end_date))

        results = cursor.fetchall()
        return results

    except mysql.connector.Error as err:
        print(f"Error fetching data: {err}")
    finally:
        cursor.close()
        mydb.close()


'''...............................................................................................................'''