import requests

from datetime import datetime

from config.config import API_KEY


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def fetch_weather_data(city):
    """
    Fetch live weather data
    from OpenWeatherMap API
    """

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        weather_info = {
            "city": city,
            "timestamp": str(
                datetime.now()
            ),
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"],
            "condition": data["weather"][0]["description"]
        }

        return weather_info

    except requests.exceptions.RequestException as e:

        print(
            f"API Error for {city}: {e}"
        )

        return None


def test_api_connection():
    """
    Test API with Mumbai
    """

    weather = fetch_weather_data(
        "Mumbai"
    )

    if weather:

        print(
            "\nAPI Connection Successful!"
        )

        print(weather)

    else:

        print(
            "\nAPI Connection Failed!"
        )
