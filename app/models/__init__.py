import psycopg2
from os import getenv


class ConnectDB:
    configs = {
        "host": getenv("DATA_HOST"),
        "user": getenv("DATA_user"),
        "database": getenv("DATA_DATABASE_NAME"),
        "password": getenv("DATA_PASSWORD")
    }

    @classmethod
    def connection_database(cls):
        cls.conn = psycopg2.connect(**cls.configs)
        cls.cur = cls.conn.cursor()
