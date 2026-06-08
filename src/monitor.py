from src.database import get_connection


def check_system_health():

    conn = get_connection()

    cursor = conn.cursor()

    try:

        cursor.execute(
            "SELECT COUNT(*) FROM cities"
        )

        city_count = cursor.fetchone()[0]

        cursor.execute(
            "SELECT COUNT(*) FROM weather_data"
        )

        weather_count = cursor.fetchone()[0]

        cursor.execute(
            "SELECT COUNT(*) FROM alerts"
        )

        alert_count = cursor.fetchone()[0]

        print("\n" + "=" * 50)
        print("WEATHER PIPELINE HEALTH REPORT")
        print("=" * 50)

        print(
            f"Cities Tracked: {city_count}"
        )

        print(
            f"Weather Records: {weather_count}"
        )

        print(
            f"Alerts Generated: {alert_count}"
        )

        print(
            "\nSystem Status: HEALTHY"
        )

    except Exception as e:

        print(
            f"\nHealth Check Failed: {e}"
        )

    finally:

        conn.close()
