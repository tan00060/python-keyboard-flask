import psycopg2
from dotenv import load_dotenv
load_dotenv()
import os

CONNECTION_PARAMETERS = {
                          'host': os.getenv("SQL_HOST"),
                          'database': os.getenv("SQL_DATABASE"),
                          'user': os.getenv("SQL_DATABASE_USER"),
                          'password': os.getenv("SQL_DATABASE_PASSWORD"),
                          'port': os.getenv("SQL_DATABASE_PORT")
}

def get_all_keycap():
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute('SELECT id, name, keycap_profile_id FROM keycap;')
            res = curs.fetchall()
            return res