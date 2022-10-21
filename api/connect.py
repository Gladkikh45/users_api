import psycopg2

try:
    conn = psycopg2.connect("dbname='pyapp' user='mediocrity' password='45863'")
    print("connected to the database.")
except:
    print("unable to connect to the database")