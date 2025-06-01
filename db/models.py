from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from .db import Base

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

class WeatherHistory(Base):
    __tablename__ = "weather_history"

    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    date = Column(Date, nullable=False)
    avgtemp_c = Column(Float(4, 1), nullable=True)
    avgtemp_f = Column(Float(4, 1), nullable=True)
    maxwind_kph = Column(Float(5, 1), nullable=True)
    maxwind_mph = Column(Float(5, 1), nullable=True)
    totalprecip_mm = Column(Float(5, 2), nullable=True)
    totalprecip_in = Column(Float(5, 2), nullable=True)

  
