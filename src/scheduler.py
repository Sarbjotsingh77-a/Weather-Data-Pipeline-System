import schedule
import time

from src.etl_pipeline import (
    run_etl_pipeline
)

from src.reporter import (
    generate_daily_report
)


def scheduled_job():

    print(
        "\nRunning Scheduled ETL Job..."
    )

    run_etl_pipeline()

    generate_daily_report()

    print(
        "\nScheduled Job Completed."
    )


def start_scheduler():

    schedule.every(
        1
    ).hours.do(
        scheduled_job
    )

    print(
        "\nScheduler Started..."
    )

    print(
        "Press CTRL + C to stop."
    )

    while True:

        schedule.run_pending()

        time.sleep(1)
