# from fastapi import FastAPI
# from routes import weather
# from services.weather_fetcher import fetch_and_store_weather
# from services.city_seeder import populate_cities
# from contextlib import asynccontextmanager
# from services.db import Base, engine

# @asynccontextmanager
# async def lifespan(_app: FastAPI):
#     # Runs once when the app starts
#     Base.metadata.create_all(bind=engine)
#     populate_cities()
#     await fetch_and_store_weather()
#     yield
#     # Runs once when the app shuts down (optional cleanup code can go here)

# app = FastAPI(lifespan=lifespan)

# @app.get("/")
# def test():
#     return {"hello": "world"}

# app.include_router(weather.router, prefix="/weather", tags=["Weather"])

from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI()

DATABASE_URL = "postgresql://postgres:postgres@db:5432/weatherdb"

engine = create_engine(DATABASE_URL)

@app.get("/cities")
def read_cities():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM cities"))
        return [dict(row) for row in result]
