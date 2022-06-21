import psycopg2
from .config import config


def save_to_db(values):
    """ Connect to the PostgreSQL database server and execute INSERT query"""
    conn = None
    query = 'INSERT INTO wine_data VALUES(%s' + ', %s'*11 + ');'
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        if len(values) == 1:
            cur.execute(query, values[0])
        else:
            cur.executemany(query, values)

        cur.execute('commit;')

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error, "Connector Module")
    finally:
        if conn is not None:
            conn.close()


def get_from_db():
    """ Connect to the PostgreSQL database server and execute SELECT query"""
    conn = None
    data = None
    query = 'SELECT * FROM wine_data;'
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.execute(query)

        data = cur.fetchall()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        return data
