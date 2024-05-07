
import mysql.connector
from mysql.connector import Error

def connect_database():
    db_name = "fitness_center_db"
    user = "root "
    password = "@Darknight1234"
    host = "127.0.0.1"

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )
        
        # if conn.is_connected():
        print("Connected to mysql Yayyy")
        return conn
    
    except Error as e:
        print(f"Error: {e}")
        return None
        
        
    # finally:
    #     if conn and conn.is_connected():
    #         conn.close()
    #         print("closed")
