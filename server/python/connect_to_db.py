import os
from dotenv import load_dotenv
import mysql.connector

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


def conn_exists():
    if get_sql_connection():
        return True
    return False


print(get_sql_connection())
