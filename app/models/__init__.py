from os import getenv

import psycopg2

config = {
    'host': getenv('DB_HOST'),
    'database': getenv('DB_NAME'),
    'user': getenv('DB_USER'),
    'password': getenv('DB_PASSWORD')
}

# conn = psycopg2.connect(**config)

class DatabaseConector:
    @classmethod
    def get_conn_cur(cls):
        cls.conn = psycopg2.connect(**config)
        cls.cur = cls.conn.cursor()

    @classmethod
    def commit_cur_conn_close(cls):
        cls.conn.commit()
        cls.cur.close()
        cls.conn.close()
