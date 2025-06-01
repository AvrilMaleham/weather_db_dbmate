-- migrate:up
CREATE TABLE IF NOT EXISTS cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    country VARCHAR NOT NULL,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION
);

INSERT INTO cities (name, country, latitude, longitude) VALUES
('Auckland', 'New Zealand', -36.8485, 174.7633),
('Sydney', 'Australia', -33.8688, 151.2093),
('London', 'UK', 51.5074, -0.1278),
('Los Angeles', 'USA', 34.0522, -118.2437),
('Bengaluru', 'India', 12.9716, 77.5946);


-- migrate:down
DROP TABLE IF EXISTS cities;

