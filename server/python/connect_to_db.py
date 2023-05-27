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
