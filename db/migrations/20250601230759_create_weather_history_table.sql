-- migrate:up
CREATE TABLE IF NOT EXISTS weather_history (
    id SERIAL PRIMARY KEY,
    city_id INTEGER NOT NULL REFERENCES cities(id),
    date DATE NOT NULL,
    avgtemp_c DECIMAL(5,1),
    avgtemp_f DECIMAL(5,1),
    maxwind_kph DECIMAL(6,1),
    maxwind_mph DECIMAL(6,1),
    totalprecip_mm DECIMAL(7,2),
    totalprecip_in DECIMAL(7,2)
);

-- Create index on city_id for better query performance
CREATE INDEX IF NOT EXISTS idx_weather_history_city_id ON weather_history(city_id);

-- Create index on date for better query performance
CREATE INDEX IF NOT EXISTS idx_weather_history_date ON weather_history(date);

-- migrate:down
DROP INDEX IF EXISTS idx_weather_history_date;
DROP INDEX IF EXISTS idx_weather_history_city_id;
DROP TABLE IF EXISTS weather_history;