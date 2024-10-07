from config import get_db_connection
from hashlib import sha256

class UserModel:
    @staticmethod
    def verify_user(username, password):
        connection = get_db_connection()
        cursor = connection.cursor()
        hashed_password = sha256(password.encode()).hexdigest()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, hashed_password))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        return user

    @staticmethod
    def create_user(first_name, last_name, username, email, password, role):
        connection = get_db_connection()
        cursor = connection.cursor()
        hashed_password = sha256(password.encode()).hexdigest()
        query = """
            INSERT INTO users (username, email, password, first_name, last_name, role) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (username, email, hashed_password, first_name, last_name, role))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def user_exists(username, email):
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username = %s OR email = %s"
        cursor.execute(query, (username, email))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        return user is not None
