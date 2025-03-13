import csv

from fastapi import FastAPI
import psycopg2

from parser import *


def connect_db():
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect('postgresql://parser_user:GeorgMax121270@127.0.0.1:5432/parser')
        return conn
        
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        raise RuntimeError('Can`t establish connection to database')
        # print('Can`t establish connection to database')


def create_table(conn):
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS data(
    id SERIAL PRIMARY KEY,
    name text,
    year text,
    spec text,
    mileage text,
    city text,
    date text            
    )
    """)
    conn.commit()


def load_data(conn, path):
    cur = conn.cursor()
    with open(path, 'r') as csv_table:
        reader = csv.reader(csv_table)
        for row in reader:
            cur.execute(
                "INSERT INTO data (name, year, spec, mileage, city, date) VALUES (%s, %s, %s, %s, %s, %s)", row)
    conn.commit()



app = FastAPI()
@app.get("/parse/")
async def parse(url):
    if 'auto.drom.ru' in url:
        filename='parsed_data.csv'
        conn = connect_db()
        create_table(conn)
        run_parser(num_pages=5, filename=filename)
        load_data(conn, filename)
        return {"message": "Parsing finished!"}
    else:
        return {'message': 'Wrong website!'}

