from airflow import DAG
from datetime import timedelta, datetime
from airflow.operators.python_operator import PythonOperator
from openweather_etl import run_openweather_etl

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'weather_dag',
    default_args=default_args,
    description='Hourly Openweather etl code',
    schedule_interval='@hourly',  
)

run_etl = PythonOperator(
    task_id='complete_openweather_etl',
    python_callable=run_openweather_etl,
    dag=dag,
)

run_etl