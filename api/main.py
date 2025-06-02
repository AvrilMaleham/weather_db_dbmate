from fastapi import FastAPI
from contextlib import asynccontextmanager
from weather_fetcher import fetch_and_store_weather
from routes import weather, cities

@asynccontextmanager
async def lifespan(_app: FastAPI):
    await fetch_and_store_weather()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def test():
    return {"hello": "world"}

app.include_router(cities.router, prefix="/cities", tags=["Cities"])
app.include_router(weather.router, prefix="/weather", tags=["Weather"])


