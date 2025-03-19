from fastapi import FastAPI
import psycopg2
import json

app = FastAPI()


def connect_db():
    try:
        conn = psycopg2.connect('postgresql://parser_user:comp_nets1470@db:5432/parser')
        return conn
        
    except:
        raise RuntimeError('Can`t establish connection to database')
    


def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id SERIAL PRIMARY KEY,
            url TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.get('/add_url/')
async def add_url(url: str):
    create_table()
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO urls (url) VALUES (%s)', (url, ))
    conn.commit()
    cur.close()
    conn.close()


@app.get('/get_urls/')
async def get_urls():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT url FROM urls')
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    data = [dict(zip(columns, row)) for row in rows]
    with open("urls.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    cur.close()
    conn.close()
