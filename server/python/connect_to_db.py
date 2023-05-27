import os
from dotenv import load_dotenv
import requests

# to load .env
from dotenv import load_dotenv
import os
import mysql.connector
import bcrypt
import uuid
# Load variables from .env file
load_dotenv()

database = os.getenv("DB")
auth_plugin = os.getenv("PLUGIN")
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")


class DBConnectionError(Exception):
    pass


def get_sql_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        auth_plugin=auth_plugin,
        database=database
    )

#
# def hash_password(password):
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
#     return hashed_password.decode('utf-8')
#
#
# hashed = '$2b$12$pL2VMNAgRz4thgREQPBbOuXh/Ya/mQVahyZ14Gy6/lWtuyGy9f1Cu'
#
#
# pw = 'password'
# bcrypt.checkpw

# print(pw.encode('utf-8'))
# print(hashed.encode('utf-8'))
# print(bcrypt.checkpw(pw.encode('utf-8'), hashed.encode('utf-8')))
#
# # if bcrypt.checkpw(pw.encode('utf-8'), hashed.encode('utf-8')):
# #     print("Password is correct.")
# # else:
# #     print("Password is incorrect.")
#
#
# # def generate_id():
# #     return uuid.uuid1()
#
#
# # word = generate_id()
#
# # print(str(word)[1:15])
# # print(len(hashed))
# email = 'abc'
# query = f'select Password where Email = {email}'
#
# print(query)
