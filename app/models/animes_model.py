import psycopg2
from app.models import DatabaseConector

class Animes(DatabaseConector):
    def __init__(self, *args, **kwargs) -> None:
        self.anime = kwargs['anime']
        self.released_date = kwargs['released_date']
        self.seasons = kwargs['seasons']

    def create_animes_model(self):
        self.get_conn_cur()

        self.cur.execute(
            """
            INSERT INTO 
                animes(anime, released_date, seasons)
            VALUES
                (%s,%s,%s)
            RETURNING *
            """, list(self.__dict__.values())
        )
        register_anime = self.cur.fetchone()

        self.conn.commit()

        self.commit_cur_conn_close()

        return register_anime
    @classmethod
    def get_all_animes(cls):
       cls.get_conn_cur()
       
       cls.cur.execute(
           """
           SELECT * FROM animes;
           """
       )

       data = cls.cur.fetchall()

       cls.commit_cur_conn_close()

       return data


    