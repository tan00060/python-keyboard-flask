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

def get_all_switch():
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            curs.execute('SELECT id, name, switch_type_id FROM switch;')
            res = curs.fetchall()
            return res

def create_switch(data):
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            try:
                curs.execute("""
                            INSERT INTO switch (name, switch_type_id)
                            VALUES (%(name)s, %(switch_type_id)s)
                            """,
                            {'name': data["name"],
                            'switch_type_id': data["switch_type_id"]
                            })
                return "Created", 200
            except Exception as e:
                return "Failed to create switch", 400

def get_switch_by_id(switch_id):
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            try:
                curs.execute("""
                            SELECT id, name, switch_type_id FROM switch WHERE ID = (%(switch_id)s)
                            """,
                            {
                            'switch_id': switch_id
                            })
                res = curs.fetchall()
                if len(res):
                    return res
                else:
                    return "Failed to find switch", 404
            except Exception as e:
                return "Failed to create switch", 400

def delete_switch(switch_id):
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            try:
                res = get_switch_by_id(switch_id)
                print(res)
                if res[-1] == 404:
                    return "Failed to delete switch", 400
                else:
                    curs.execute("""
                                DELETE FROM switch WHERE ID = (%(switch_id)s)
                                """,
                                {
                                'switch_id': switch_id
                                })
                    return "Deleted Switch", 200
            except Exception as e:
                return "Failed to create switch", 400

def update_by_id_switch(switch_id, body):
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as curs:
            try:
                res = get_switch_by_id(switch_id)
                print(res)
                if res[-1] == 404:
                    return "Failed to update switch", 400
                else:
                    curs.execute("""
                                UPDATE switch SET name=(%(name)s) WHERE ID =(%(switch_id)s)
                                """,
                                {
                                'switch_id': switch_id,
                                'name': body["name"]
                                })
                    return "Updated Switch", 200
            except Exception as e:
                return "Failed to update switch", 400