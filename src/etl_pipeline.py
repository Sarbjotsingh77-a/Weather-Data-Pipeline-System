from config.config import (
    TRACKED_CITIES,
    TEMPERATURE_ALERT_THRESHOLD,
    HUMIDITY_ALERT_THRESHOLD
)

from src.api_client import fetch_weather_data
from src.validators import validate_weather_record

from src.database import (
    insert_city,
    get_city_id,
    insert_weather_data,
    insert_alert
)


def process_city(city):
    """
    Extract weather data
    """

    weather = fetch_weather_data(city)

    if weather is None:

        print(
            f"Failed to fetch data for {city}"
        )

        return

    """
    Validate data
    """

    if not validate_weather_record(weather):

        print(
            f"Validation failed for {city}"
        )

        return

    """
    Store city
    """

    insert_city(city)

    city_id = get_city_id(city)

    """
    Load weather data
    """

    insert_weather_data(
        city_id,
        weather["timestamp"],
        weather["temperature"],
        weather["humidity"],
        weather["pressure"],
        weather["wind_speed"],
        weather["condition"]
    )

    print(
        f"Weather data stored for {city}"
    )

    """
    Generate alerts
    """

    if (
        weather["temperature"]
        >
        TEMPERATURE_ALERT_THRESHOLD
    ):

        insert_alert(
            city_id,
            "Temperature Alert",
            (
                f"{city}: "
                f"{weather['temperature']}°C "
                f"exceeded threshold"
            )
        )

    if (
        weather["humidity"]
        >
        HUMIDITY_ALERT_THRESHOLD
    ):

        insert_alert(
            city_id,
            "Humidity Alert",
            (
                f"{city}: "
                f"{weather['humidity']}% "
                f"exceeded threshold"
            )
        )


def run_etl_pipeline():
    """
    Main ETL workflow
    """

    print(
        "\nStarting ETL Pipeline..."
    )

    for city in TRACKED_CITIES:

        process_city(city)

    print(
        "\nETL Pipeline Completed Successfully!"
    )
