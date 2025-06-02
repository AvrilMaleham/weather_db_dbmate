import psycopg2
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_weather_history():
    conn = psycopg2.connect("dbname=weatherdb user=postgres password=postgres host=db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM weather_history")
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    results = [dict(zip(columns, row)) for row in rows]
    cur.close()
    conn.close()
    return results