## Overview
This project implements an end-to-end data pipeline using Apache Airflow to extract, transform, and load Twitter data into an AWS S3 bucket. It automates the ETL process by running on an AWS EC2 instance.

Credit: This project is originally from Darshil Parmar and I have successfully executed it.

## Features
- Extracts tweets from Twitter using Tweepy
- Transforms data into structured format using Pandas
- Stores processed data into AWS S3
- Automates the pipeline with Apache Airflow

## Architecture
- Extract: Fetch tweets using the Twitter API.
- Transform: Convert tweet data into a structured Pandas DataFrame.
- Load: Store processed data in an AWS S3 bucket.
- Orchestrate: Use Apache Airflow on an AWS EC2 instance to automate the pipeline.
![Untitled design](https://github.com/user-attachments/assets/68932fb8-a4f2-46f7-86bd-138484d7551c)
