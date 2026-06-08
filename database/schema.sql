CREATE TABLE IF NOT EXISTS cities (
    city_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name TEXT NOT NULL,
    country TEXT,
    latitude REAL,
    longitude REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS weather_data (
    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER,
    timestamp TEXT,
    temperature REAL,
    humidity INTEGER,
    pressure REAL,
    wind_speed REAL,
    condition TEXT,
    FOREIGN KEY(city_id) REFERENCES cities(city_id)
);

CREATE TABLE IF NOT EXISTS alerts (
    alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_id INTEGER,
    alert_type TEXT,
    alert_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(city_id) REFERENCES cities(city_id)
);
