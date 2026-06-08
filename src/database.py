import sqlite3
from config.config import DATABASE_NAME


def get_connection():
    """
    Create and return database connection
    """
    return sqlite3.connect(DATABASE_NAME)


def setup_database():
    """
    Create all required tables
    """

    conn = get_connection()

    cursor = conn.cursor()

    # Cities Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cities (
        city_id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_name TEXT NOT NULL UNIQUE,
        country TEXT,
        latitude REAL,
        longitude REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Weather Data Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_data (
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_id INTEGER,
        timestamp TEXT,
        temperature REAL,
        humidity INTEGER,
        pressure REAL,
        wind_speed REAL,
        weather_condition TEXT,
        FOREIGN KEY(city_id)
        REFERENCES cities(city_id)
    )
    """)

    # Alerts Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alerts (
        alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_id INTEGER,
        alert_type TEXT,
        alert_message TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(city_id)
        REFERENCES cities(city_id)
    )
    """)

    conn.commit()
    conn.close()

    print("✅ Database setup completed successfully.")


def insert_city(city_name):
    """
    Insert city if not exists
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO cities(city_name)
        VALUES(?)
        """,
        (city_name,)
    )

    conn.commit()
    conn.close()


def get_city_id(city_name):
    """
    Get city ID from city name
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT city_id
        FROM cities
        WHERE city_name = ?
        """,
        (city_name,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return None


def insert_weather_data(
    city_id,
    timestamp,
    temperature,
    humidity,
    pressure,
    wind_speed,
    weather_condition
):
    """
    Store weather data
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO weather_data(
            city_id,
            timestamp,
            temperature,
            humidity,
            pressure,
            wind_speed,
            weather_condition
        )
        VALUES(?,?,?,?,?,?,?)
        """,
        (
            city_id,
            timestamp,
            temperature,
            humidity,
            pressure,
            wind_speed,
            weather_condition
        )
    )

    conn.commit()
    conn.close()


def insert_alert(
    city_id,
    alert_type,
    alert_message
):
    """
    Store generated alerts
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO alerts(
            city_id,
            alert_type,
            alert_message
        )
        VALUES(?,?,?)
        """,
        (
            city_id,
            alert_type,
            alert_message
        )
    )

    conn.commit()
    conn.close()


def get_weather_records():
    """
    Retrieve all weather records
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM weather_data
        """
    )

    records = cursor.fetchall()

    conn.close()

    return records
