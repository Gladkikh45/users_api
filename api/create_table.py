import psycopg2
from psycopg2.extras import RealDictCursor

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

try:
    cur.execute("""
    select user_if, from main.users;
    """)
    records = cur.fetchall()
    # conn.commit()
except Exception as err:
    print(err)


for row in records:
    print(row.get("id"))