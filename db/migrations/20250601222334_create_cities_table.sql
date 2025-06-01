-- migrate:up
CREATE TABLE IF NOT EXISTS cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country VARCHAR(100) NOT NULL,
    latitude DECIMAL(8,6),
    longitude DECIMAL(9,6),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(name, country)
);

-- Create index for geographic queries
CREATE INDEX IF NOT EXISTS idx_cities_coordinates ON cities(latitude, longitude);

-- Insert seed data only if table is empty
INSERT INTO cities (name, country, latitude, longitude) 
SELECT * FROM (VALUES
    ('Auckland', 'New Zealand', -36.848500, 174.763300),
    ('Sydney', 'Australia', -33.868800, 151.209300),
    ('London', 'UK', 51.507400, -0.127800),
    ('Los Angeles', 'USA', 34.052200, -118.243700),
    ('Bengaluru', 'India', 12.971600, 77.594600)
) AS new_cities(name, country, latitude, longitude)
WHERE NOT EXISTS (SELECT 1 FROM cities LIMIT 1);

-- migrate:down
DROP INDEX IF EXISTS idx_cities_coordinates;
DROP TABLE IF EXISTS cities;

