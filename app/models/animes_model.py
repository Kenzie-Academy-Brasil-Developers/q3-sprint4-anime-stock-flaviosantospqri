import psycopg2
from app.models import DatabaseConector
from psycopg2 import sql


class Animes(DatabaseConector):
    animes_keys = ["id", "anime", "released_date", "seasons"]
    def __init__(self, *args, **kwargs) -> None:
        self.anime = kwargs['anime'].title()
        self.released_date = kwargs['released_date']
        self.seasons = kwargs['seasons']

    @classmethod
    def create_table_base(cls):
        cls.get_conn_cur()
        cls.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS animes(
            id BIGSERIAL PRIMARY KEY,
            anime VARCHAR(100) NOT NULL UNIQUE,
            released_date DATE NOT NULL,
            seasons INTEGER NOT NULL
            );
            """
        )
    @classmethod
    def patch_animes(cls, id, payload):
        cls.get_conn_cur()
        cls.create_table_base()

        columns = [sql.Identifier(key) for key in payload.keys()]

        values = [sql.Literal(value) for value in payload.values()]

        query = sql.SQL(
            """
                UPDATE 
                    animes
                SET
                    ({columns}) = ROW({values})
                WHERE 
                    id={id}
                RETURNING *
            """
        ).format(
            id=sql.Literal(id),
            columns=sql.SQL(",").join(columns),
            values=sql.SQL(",").join(values),
        )
        cls.cur.execute(query)
        
        update_anime = cls.cur.fetchone()
        
        cls.commit_cur_conn_close()
        
        return update_anime
    
    @classmethod
    def find_anime(cls, id):
        cls.get_conn_cur()
        cls.create_table_base()


        query = sql.SQL(
            """
                SELECT * FROM animes
                WHERE 
                    id={id}
            """
        ).format(
            id=sql.Literal(id)
        )
        cls.cur.execute(query)
        
        finded_anime = cls.cur.fetchone()

        cls.commit_cur_conn_close()
        
        return finded_anime


    @classmethod
    def delete_animes(cls, id):
        cls.get_conn_cur()
        cls.create_table_base()

        query = sql.SQL(
            """
                DELETE FROM animes
                WHERE 
                    id={id}
                RETURNING *
            """
        ).format(
            id=sql.Literal(id)
        )
        cls.cur.execute(query)
        
        deleted_anime = cls.cur.fetchone()
        
        cls.commit_cur_conn_close()
        
        return deleted_anime
    
    
    @staticmethod
    def serialize_method(data, keys = animes_keys):
        if type(data) is tuple:
            return dict(zip(keys, data))
        if type(data) is list:
            return [dict(zip(keys, anime)) for anime in data]

    def create_animes_model(self):
        self.get_conn_cur()
        self.create_table_base()
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
       cls.create_table_base()
       cls.cur.execute(
           """
           SELECT * FROM animes;
           """
       )

       data = cls.cur.fetchall()

       cls.commit_cur_conn_close()

       return data


    