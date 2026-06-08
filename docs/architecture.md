# System Architecture

The Weather Data Pipeline System follows an ETL architecture.

Workflow:

1. Extract weather data from OpenWeatherMap API.
2. Validate incoming data.
3. Transform and clean records.
4. Load data into SQLite database.
5. Generate reports and alerts.
6. Monitor system health.

Components:
- API Client
- ETL Pipeline
- Database Layer
- Reporting Module
- Monitoring Module
- Scheduler
