## Overview
This project implements an end-to-end data pipeline using Apache Airflow to extract, transform, and load OpenWeather data into an AWS S3 bucket. It automates the ETL process by running on an AWS EC2 instance.

## Features
- Pipeline gathers Data from OpenWeather API
- Transforms data into a structured format using Pandas
- Stores processed data into AWS S3
- Automates the pipeline with Apache Airflow
- Captures hourly data to analyze trends and fluctuations.

## Architecture
- Extract: Fetch Data using the OpenWeather API.
- Transform: Convert weather data into a structured Pandas DataFrame.
- Load: Store processed data in an AWS S3 bucket.
- Orchestrate: Use Apache Airflow on an AWS EC2 instance to automate the pipeline.
![Untitled design](https://github.com/user-attachments/assets/68932fb8-a4f2-46f7-86bd-138484d7551c)
