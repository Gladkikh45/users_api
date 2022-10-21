import psycopg2
from psycopg2.extras import RealDictCursor


def get_cursor():
    try:
        conn = psycopg2.connect(
            dbname='postgres', 
            user='postgres', 
            password='1234', 
            host='localhost',
            port=5442,
            )
    except:
        print("unable to connect to the database")


    cur = conn.cursor(cursor_factory=RealDictCursor)
    return cur, conn
