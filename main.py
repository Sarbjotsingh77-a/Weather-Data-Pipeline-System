from src.database import setup_database
from src.etl_pipeline import run_etl_pipeline
from src.reporter import generate_daily_report
from src.monitor import check_system_health
from src.scheduler import start_scheduler


def display_menu():
    print("\n" + "=" * 50)
    print("      WEATHER DATA PIPELINE SYSTEM")
    print("=" * 50)
    print("1. Setup Database")
    print("2. Run ETL Pipeline")
    print("3. Generate Daily Report")
    print("4. System Health Check")
    print("5. Start Scheduler")
    print("6. Exit")


def main():

    while True:

        display_menu()

        choice = input(
            "\nEnter your choice (1-6): "
        )

        if choice == "1":

            try:
                setup_database()
                print(
                    "\n✅ Database setup completed successfully."
                )

            except Exception as e:

                print(
                    f"\n❌ Database Error: {e}"
                )

        elif choice == "2":

            try:
                run_etl_pipeline()

                print(
                    "\n✅ ETL Pipeline executed successfully."
                )

            except Exception as e:

                print(
                    f"\n❌ ETL Error: {e}"
                )

        elif choice == "3":

            try:

                generate_daily_report()

                print(
                    "\n✅ Report generated successfully."
                )

            except Exception as e:

                print(
                    f"\n❌ Report Error: {e}"
                )

        elif choice == "4":

            try:

                check_system_health()

            except Exception as e:

                print(
                    f"\n❌ Monitoring Error: {e}"
                )

        elif choice == "5":

            try:

                print(
                    "\n⏰ Scheduler Started..."
                )

                start_scheduler()

            except Exception as e:

                print(
                    f"\n❌ Scheduler Error: {e}"
                )

        elif choice == "6":

            print(
                "\nThank you for using Weather Data Pipeline System!"
            )

            break

        else:

            print(
                "\n❌ Invalid Choice. Please select 1-6."
            )


if __name__ == "__main__":
    main()
