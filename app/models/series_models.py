from typing import Literal
import psycopg2
from psycopg2 import sql
from app.models import ConnectDB

class Series(ConnectDB):
    def __init__(self, **kwargs):
        self.serie = kwargs["serie"]
        self.seasons = kwargs["seasons"]
        self.released_date = kwargs["released_date"]
        self.genre = kwargs["genre"]
        self.imdb_rating = kwargs["imdb_rating"]


    @classmethod
    def writer_series(cls, data):
        cls.connection_database()

        cls.cur.execute("""
            CREATE TABLE IF NOT EXISTS ka_series (
                id BIGSERIAL PRIMARY KEY,
                serie VARCHAR(100) NOT NULL UNIQUE,
                seasons INTEGER NOT NULL,
                released_date DATE NOT NULL,
                genre VARCHAR(50) NOT NULL,
                imdb_rating FLOAT NOT NULL
            );
        """)

        query = """
            INSERT INTO ka_series
                (serie, seasons, released_date, genre, imdb_rating)
            VALUES
                (%s, %s, %s, %s, %s)
            RETURNING *;
        """

        values = (data["serie"].title(), data["seasons"], data["released_date"], data["genre"].title(), data["imdb_rating"])

        cls.cur.execute(query, values)

        data_request = cls.cur.fetchone()

        cls.conn.commit()

        cls.cur.close()
        cls.conn.close()

        return data_request


    @classmethod
    def reader_series(cls):
        cls.connection_database()

        cls.cur.execute("""
            CREATE TABLE IF NOT EXISTS ka_series (
                id BIGSERIAL PRIMARY KEY,
                serie VARCHAR(100) NOT NULL UNIQUE,
                seasons INTEGER NOT NULL,
                released_date DATE NOT NULL,
                genre VARCHAR(50) NOT NULL,
                imdb_rating FLOAT NOT NULL
            );
        """)

        cls.cur.execute("""
            SELECT
                *
            FROM
                ka_series
            ORDER BY
                id;
        """)

        data = cls.cur.fetchall()

        fieldnames = ["id", "serie", "seasons", "released_date", "genre", "imdb_rating"]
        values = [dict(zip(fieldnames, dt)) for dt in data]

        cls.conn.commit()

        cls.cur.close()
        cls.conn.close()

        return values


    @classmethod
    def reader_series_by_id(cls, id):
        cls.connection_database()

        cls.cur.execute("""
            CREATE TABLE IF NOT EXISTS ka_series (
                id BIGSERIAL PRIMARY KEY,
                serie VARCHAR(100) NOT NULL UNIQUE,
                seasons INTEGER NOT NULL,
                released_date DATE NOT NULL,
                genre VARCHAR(50) NOT NULL,
                imdb_rating FLOAT NOT NULL
            );
        """)

        query = sql.SQL("""
            SELECT
                *
            FROM
                ka_series
            WHERE
                id = {id}
        """).format(
            id = sql.Literal(id)
        )

        cls.cur.execute(query)

        data = cls.cur.fetchone()

        cls.cur.close()
        cls.conn.close()

        return data

