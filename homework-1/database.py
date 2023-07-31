import psycopg2
import csv
import os

conn = psycopg2.connect(host='localhost', database="north", user="postgres", password=os.getenv("pgAdmin"))


def instert_to_db(file_path, quary):
    with open(file_path) as file:
        reader = csv.reader(file)
        next(reader)
        with conn.cursor() as curs:
            curs.executemany(quary, reader)
    conn.commit()
