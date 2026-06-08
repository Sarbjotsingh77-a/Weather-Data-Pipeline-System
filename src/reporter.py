import os

from src.database import (
    get_connection
)


REPORTS_DIR = "reports"


def generate_daily_report():

    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        c.city_name,
        w.temperature,
        w.humidity,
        w.pressure,
        w.wind_speed,
        w.weather_condition,
        w.timestamp
    FROM weather_data w
    JOIN cities c
    ON w.city_id = c.city_id
    ORDER BY w.record_id DESC
    LIMIT 20
    """)

    records = cursor.fetchall()

    report_path = (
        "reports/daily_report.txt"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "DAILY WEATHER REPORT\n"
        )

        file.write(
            "=" * 50 + "\n\n"
        )

        for row in records:

            file.write(
                f"City: {row[0]}\n"
            )

            file.write(
                f"Temperature: {row[1]}°C\n"
            )

            file.write(
                f"Humidity: {row[2]}%\n"
            )

            file.write(
                f"Pressure: {row[3]} hPa\n"
            )

            file.write(
                f"Wind Speed: {row[4]} m/s\n"
            )

            file.write(
                f"Condition: {row[5]}\n"
            )

            file.write(
                f"Timestamp: {row[6]}\n"
            )

            file.write(
                "-" * 40 + "\n"
            )

    conn.close()

    print(
        "Daily report generated successfully."
    )


def generate_alerts_report():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        alert_type,
        alert_message,
        created_at
    FROM alerts
    ORDER BY alert_id DESC
    """)

    alerts = cursor.fetchall()

    report_path = (
        "reports/alerts_report.txt"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "ALERTS REPORT\n"
        )

        file.write(
            "=" * 50 + "\n\n"
        )

        for alert in alerts:

            file.write(
                f"{alert[0]}\n"
            )

            file.write(
                f"{alert[1]}\n"
            )

            file.write(
                f"{alert[2]}\n"
            )

            file.write(
                "-" * 40 + "\n"
            )

    conn.close()

    print(
        "Alerts report generated successfully."
    )


def generate_weekly_report():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        AVG(temperature),
        AVG(humidity),
        AVG(pressure),
        AVG(wind_speed)
    FROM weather_data
    """)

    result = cursor.fetchone()

    report_path = (
        "reports/weekly_report.txt"
    )

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "WEEKLY WEATHER SUMMARY\n"
        )

        file.write(
            "=" * 50 + "\n\n"
        )

        file.write(
            f"Average Temperature: {result[0]:.2f}°C\n"
        )

        file.write(
            f"Average Humidity: {result[1]:.2f}%\n"
        )

        file.write(
            f"Average Pressure: {result[2]:.2f} hPa\n"
        )

        file.write(
            f"Average Wind Speed: {result[3]:.2f} m/s\n"
        )

    conn.close()

    print(
        "Weekly report generated successfully."
    )
