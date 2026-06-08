from src.database import setup_database
from src.etl_pipeline import run_etl_pipeline

setup_database()

run_etl_pipeline()
