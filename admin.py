import mysql.connector

def authenticate(user, password):

    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user=user,
            password=password
        )
        cursor = cnx.cursor()
        return True
    except mysql.connector.Error as err:
        print(f"Authentication failed: {err}")
        return False

