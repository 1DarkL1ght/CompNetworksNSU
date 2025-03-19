import csv

from fastapi import FastAPI
import psycopg2
import json

from parser import *


def connect_db():
    try:
        conn = psycopg2.connect('postgresql://parser_user:comp_nets1470@127.0.0.1:5432/parser')
        return conn
        
    except:
        raise RuntimeError('Can`t establish connection to database')


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
    cur.close()
    conn.close()



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


@app.get("/json/")
async def get_json():
    table_name = 'data'
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {table_name}')

    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    data = [dict(zip(columns, row)) for row in rows]

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    cur.close()
    conn.close()