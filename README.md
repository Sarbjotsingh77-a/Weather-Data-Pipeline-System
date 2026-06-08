# 🌦️ Weather Data Pipeline System

## Project Overview

The Weather Data Pipeline System is an end-to-end data engineering project developed using Python, SQLite, APIs, and ETL (Extract, Transform, Load) processes. The system automatically collects weather data from external APIs, validates and transforms the data, stores it in a normalized database, and generates reports and alerts for monitoring and analysis.

This project demonstrates practical skills in database management, API integration, SQL, ETL workflows, scheduling, data validation, logging, and automation.

---

## Objectives

* Extract weather data from APIs
* Transform and validate incoming data
* Store data in a normalized SQLite database
* Generate automated reports and alerts
* Implement scheduling and monitoring
* Perform historical weather analysis

---

## Technologies Used

* Python
* SQLite
* Requests
* Pandas
* Schedule
* SQL
* GitHub

---

## Project Structure

```text
Weather-Data-Pipeline-System/
│
├── README.md
├── requirements.txt
├── main.py
│
├── config/
├── src/
├── database/
├── sample_data/
├── logs/
├── reports/
├── tests/
├── docs/
├── screenshots/
└── scripts/
```

---

## Features

### Data Collection

* Weather API Integration
* Multi-city weather tracking
* Automated data extraction

### Data Validation

* Missing value checks
* Data type validation
* Range validation

### Database Management

* SQLite database
* Normalized schema
* Historical data storage

### Reporting

* Daily weather reports
* Weekly summary reports
* Alert generation

### Monitoring

* Pipeline status tracking
* Error logging
* Health checks

---

## Database Schema

### Cities Table

| Column    | Type    |
| --------- | ------- |
| city_id   | INTEGER |
| city_name | TEXT    |
| country   | TEXT    |
| latitude  | REAL    |
| longitude | REAL    |

### Weather Data Table

| Column      | Type    |
| ----------- | ------- |
| record_id   | INTEGER |
| city_id     | INTEGER |
| timestamp   | TEXT    |
| temperature | REAL    |
| humidity    | INTEGER |
| pressure    | REAL    |
| wind_speed  | REAL    |
| condition   | TEXT    |

### Alerts Table

| Column        | Type    |
| ------------- | ------- |
| alert_id      | INTEGER |
| city_id       | INTEGER |
| alert_type    | TEXT    |
| alert_message | TEXT    |
| created_at    | TEXT    |

---

## ETL Workflow

### Extract

* Fetch weather data from API
* Parse JSON responses

### Transform

* Clean data
* Validate records
* Format timestamps

### Load

* Store processed data in SQLite database
* Generate alerts if thresholds are exceeded

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Weather-Data-Pipeline-System.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python main.py
```

---

## Reports Generated

* Daily Weather Report
* Weekly Weather Summary
* Alerts Report

---

## Testing

The project includes test modules for:

* Database Operations
* API Integration
* ETL Pipeline
* Data Validation

Run tests using:

```bash
python tests/test_database.py
```

---

## Learning Outcomes

* Database Design
* SQL Fundamentals
* API Integration
* ETL Development
* Data Validation
* Scheduling and Automation
* Monitoring and Logging
* Python Project Structure

---

## Future Improvements

* Real-time dashboard
* Cloud database integration
* Email notifications
* Advanced analytics
* Multi-API support

---

## Author

**Sarbjot Singh**

B.Tech (AI & Data Science)

---

## License

This project is developed for educational and internship learning purposes.
