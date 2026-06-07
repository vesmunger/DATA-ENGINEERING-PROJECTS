# Data Engineering Projects

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat&logo=apache-airflow&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat&logo=apache-kafka&logoColor=white)
![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)

**Author:** vesmunger 

## Technologies & Tools Used

### Programming Languages
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/-SQL-4479A1?style=flat&logo=postgresql&logoColor=white)

### Data Storage & Platforms
![MongoDB](https://img.shields.io/badge/-MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-316192?style=flat&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/-MySQL-4479A1?style=flat&logo=mysql&logoColor=white)
![AWS](https://img.shields.io/badge/-AWS-232F3E?style=flat&logo=amazon-aws&logoColor=white)
![Azure](https://img.shields.io/badge/-Azure-0078D4?style=flat&logo=microsoft-azure&logoColor=white)

### Data & Workflow Tools
![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/-Airflow-017CEE?style=flat&logo=apache-airflow&logoColor=white)
![Apache Kafka](https://img.shields.io/badge/-Kafka-231F20?style=flat&logo=apache-kafka&logoColor=white)
![Git](https://img.shields.io/badge/-Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat&logo=github&logoColor=white)
![Grafana](https://img.shields.io/badge/-Grafana-F46800?style=flat&logo=grafana&logoColor=white)

---

## Overview
This repository contains a collection of **data engineering projects** :ETL/ELT pipelines, API integration, real-time streaming, data transformation, and storage. Projects showcase Python, SQL, Pandas, MongoDB, Airflow, Kafka, and cloud platforms, AWS and Azure.  

The projects are somehow organized to reflect **real-world scenarios**, including financial, weather, and general-purpose datasets.

---

## Projects

### 1. Faker Data Generator
- **Description**: Generates synthetic datasets for testing pipelines, including names, addresses, and random attributes.  
- **Technologies**: Python, Pandas.  
- **Key Skills**: Data simulation, testing ETL pipelines, data modeling.

### 2. Gas Prices API
- **Description**: Scrapes gas price data from [CollectAPI](https://collectapi.com/) and stores it in MongoDB and optionally PostgreSQL.  
- **Technologies**: Python, Pandas, MongoDB, SQLAlchemy.  
- **Key Skills**: API ingestion, ETL, data cleaning, data storage, workflow automation.

### 3. OpenWeather API & Streaming
- **Description**: Pulls current weather data and forecasts using OpenWeather API; can stream data periodically using cron or Airflow.  
- **Technologies**: Python, Pandas, MongoDB, Airflow.  
- **Key Skills**: Real-time data ingestion, ETL pipelines, scheduling jobs, data visualization preparation.

### 4. Weather Data with Airflow
- **Description**: Automated ETL workflow to fetch, transform, and store weather data daily using Airflow DAGs.  
- **Technologies**: Python, Airflow, Pandas, MongoDB.  
- **Key Skills**: Workflow orchestration, ETL automation, XCom usage, production-ready pipelines.

### 5. Crypto Data with Airflow
- **Description**: Real-time cryptocurrency data ingestion using CoinGecko API and Airflow DAGs; data stored in MongoDB.  
- **Technologies**: Python, Airflow, Pandas, MongoDB.  
- **Key Skills**: Scheduled workflows, API integration, real-time financial data, ETL pipelines.

### 6. Binance Data Project
- **Description**: Fetches financial market data from Binance API endpoints, including 24hr ticker, live prices, klines, order depth, and trades; stores data in MongoDB.  
- **Technologies**: Python, Requests, MongoDB, dotenv.  
- **Key Skills**: Real-time financial data ingestion, API integration, MongoDB storage, data analytics readiness.

---

## Features Demonstrated
- Data ingestion from multiple APIs (Binance, CoinGecko, CollectAPI, OpenWeather)
- ETL and ELT pipelines with scheduling (Airflow, Cron)
- Real-time data streaming with Kafka
- Data storage in MongoDB and relational databases (PostgreSQL, MySQL)
- Data cleaning, transformation, and visualization
- Python programming and Pandas for analytics
- Automation of repetitive workflows

---

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/vesmunger/DATA-ENGINEERING-PROJECTS.git

## License
This repository is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).
