from connect_to_db import get_sql_connection, DBConnectionError
import bcrypt
import uuid


class User:
    def __init__(self, first_name, last_name, email, phone_no, dob, address, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_no = phone_no
        self.dob = dob
        self.address = address
        self.password = password

    def get_data(self):
        return {
            self.address,
            self.first_name,
            self.last_name,
            self.email,
            self.dob,
            self.phone_no,
            self.password
        }

    @staticmethod
    def get_users():
        conn = None
        try:
            conn = get_sql_connection()
            cursor = conn.cursor(dictionary=True)
            query = 'select * from users'
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as exc:
            raise DBConnectionError('Failed to connect to database') from exc
        finally:
            if conn:
                conn.close()

    def get_user_id(self):
        conn = None
        try:
            conn = get_sql_connection()
            cursor = conn.cursor()
            query = f"select UserId from Users where Email = '{self.email}'"
            cursor.execute(query)
            u_id = cursor.fetchone()
            if u_id:
                return u_id[0]
            else:
                return self.generate_id()
        except Exception as exc:
            raise DBConnectionError('Failed to connect to database') from exc
        finally:
            if conn:
                conn.close()

    @staticmethod
    def get_user_by_id(u_id):
        conn = None
        try:
            conn = get_sql_connection()
            cursor = conn.cursor(dictionary=True)
            query = f'select * from users where UserId = "{u_id}"'
            cursor.execute(query)
            return cursor.fetchone()
        except Exception as exc:
            raise DBConnectionError('Failed to connect to database') from exc
        finally:
            if conn:
                conn.close()

    def login(self, data):
        conn = None
        try:
            conn = get_sql_connection()
            cursor = conn.cursor(dictionary=True)
            query = f"select * from Users where Email = '{data['Email']}'"
            cursor.execute(query)
            pw = cursor.fetchone()
            verify_pw = self.verify_password(data['Password'], pw['Password'])
            if verify_pw:
                return {**pw, 'status': 'success'}
            else:
                return 'Incorrect Username or Password'
        except Exception as exc:
            raise DBConnectionError('Failed to connect to database') from exc
        finally:
            if conn:
                conn.close()

    @staticmethod
    def hash_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    @staticmethod
    def verify_password(user_pw, db_pw):
        db_pw = db_pw.encode('utf-8')
        pw_input = user_pw.encode('utf-8')
        correct_pw = bcrypt.checkpw(pw_input, db_pw)
        return correct_pw

    @staticmethod
    def decode_password(password):
        return password.encode('utf-8')

    @staticmethod
    def generate_id():
        u_id = uuid.uuid4()
        return str(u_id)

    def add_user(self, data):
        conn = None
        try:
            conn = get_sql_connection()
            cursor = conn.cursor(dictionary=True)
            query = f"INSERT INTO Users (UserId, FirstName, LastName, Email, PhoneNo, " \
                    f"Dob, Address, Password) VALUES " \
                    f"('{self.generate_id()}', '{data['FirstName']}', '{data['LastName']}', '{data['Email']}', " \
                    f"'{data['PhoneNo']}', '{data['Dob']}', '{data['Address']}', '{self.hash_password(data['Password'])}');"
            cursor.execute(query)
            conn.commit()
            cursor.close()
            return {**data, 'status': 'success', 'message': 'user added successfully'}
        except Exception as exc:
            raise DBConnectionError('Failed to connect to database') from exc
        finally:
            if conn:
                conn.close()

    def does_user_exist(self, data):
        users = self.get_users()
        count = 0
        for singleUser in users:
            if data['Email'] == singleUser['Email']:
                count += 1
        return True if count == 1 else False

    @staticmethod
    def remove_user(u_id):
        conn = None
        try:
            conn = get_sql_connection()
            cursor = conn.cursor(dictionary=True)
            query = f"DELETE FROM users WHERE UserId = '{u_id}'"
            cursor.execute(query)
            conn.commit()
            cursor.close()
        except Exception as exc:
            raise DBConnectionError('Failed to connect to database') from exc
        finally:
            if conn:
                conn.close()


user = User(
    "Emina",
    "Ergul",
    "emina.ergul@example.com",
    "+1234567890",
    "1990-01-01",
    "123 Main Street, City, Country",
    "password123",
)


data = {
    "FirstName": "Joanne",
    "LastName": "Leow",
    "Email": "feranmi.ayo@example.com",
    "PhoneNo": "+3234567890",
    "Dob": "1993-01-01",
    "Address": "123 Leow Street, City, Country",
    "Password": "password123",
}


# print(user.add_user(data))
