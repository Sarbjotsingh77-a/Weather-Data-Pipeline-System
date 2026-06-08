import shutil

try:

    shutil.copy(
        "database/weather_data.db",
        "database/weather_backup.db"
    )

    print(
        "Database backup completed successfully."
    )

except Exception as e:

    print(
        f"Backup Error: {e}"
    )
