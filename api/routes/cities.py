from fastapi import APIRouter
from sqlalchemy import create_engine, text

router = APIRouter()

DATABASE_URL = "postgresql://postgres:postgres@db:5432/weatherdb"

engine = create_engine(DATABASE_URL)

@router.get("/")
def read_cities():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM cities"))
        return [dict(row._mapping) for row in result]