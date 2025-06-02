import httpx
import psycopg2
from datetime import datetime, timedelta

DATABASE_URL = "postgresql://postgres:postgres@db:5432/weatherdb"

def get_most_recent_7_days():
    today = datetime.today()
    end_date = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    start_date = (today - timedelta(days=13)).strftime('%Y-%m-%d')
    return start_date, end_date

async def fetch_and_store_weather():
    start_date, end_date = get_most_recent_7_days()

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    try:
        cur.execute("SELECT id, latitude, longitude FROM cities")
        cities = cur.fetchall()  

        async with httpx.AsyncClient() as client:
            for city_id, lat, lon in cities:
                url = (
                    f"https://archive-api.open-meteo.com/v1/archive?"
                    f"latitude={lat}&longitude={lon}&start_date={start_date}"
                    f"&end_date={end_date}"
                    f"&daily=temperature_2m_mean,windspeed_10m_max,precipitation_sum"
                    f"&timezone=auto"
                )

                response = await client.get(url)
                data = response.json()

                dates = data["daily"]["time"]
                temps_c = data["daily"]["temperature_2m_mean"]
                wind_kph = data["daily"]["windspeed_10m_max"]
                precip_mm = data["daily"]["precipitation_sum"]

                for date, temp_c, wind_k, precip_m in zip(dates, temps_c, wind_kph, precip_mm):
                    date_obj = datetime.strptime(date, "%Y-%m-%d").date()
                    temp_f = round((temp_c * 9 / 5) + 32, 1)
                    wind_mph = round(wind_k * 0.621371, 1)
                    precip_in = round(precip_m / 25.4, 2)

                    cur.execute("""
                        INSERT INTO weather_history (
                            city_id, date, avgtemp_c, avgtemp_f,
                            maxwind_kph, maxwind_mph, totalprecip_mm, totalprecip_in
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT DO NOTHING
                    """, (
                        city_id, date_obj, round(temp_c, 1), temp_f,
                        round(wind_k, 1), wind_mph, round(precip_m, 2), precip_in
                    ))

        conn.commit()
    finally:
        cur.close()
        conn.close()
