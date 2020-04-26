from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from get_tweets_related.get_tweets import get_tweets
from s3_push_related.push_tweets_to_s3 import push_tweets_to_s3


default_args = {
    "owner": "me",
    "depends_on_past": False,
    "start_date": datetime(2020, 4, 4),
    "email": ["my_email@mail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
    "schedule_interval": "10 * * * *",
}

with DAG("twitter_tweets_daily", default_args=default_args) as dag:

    Task_I = PythonOperator(
        task_id='get_tweets', python_callable=get_tweets 
    )
    Task_II = BashOperator(
        task_id='print_something', bash_command='echo "{{ ds }}" && sleep 1')
        #'echo "{{ params.file }}" && sleep 1' , params={'file':'{{ ds }}'}  
        #bash_command='echo  "Welcome to Airflow !!!!"' 
        
    Task_III = PythonOperator(
        task_id="push_tweets_to_s3", python_callable=push_tweets_to_s3
    )  
Task_II >> Task_I >> Task_III


