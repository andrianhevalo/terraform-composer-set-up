from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from datetime import timedelta, datetime


default_args = {
    'owner': 'andrian.hevalo',    
    'depends_on_past': False,
    'email': ['andrianhevalo@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    }

with DAG("custom_dag", 
    start_date=datetime(2022, 8, 4)) as dag:


    start = DummyOperator(task_id="pipeline_start", trigger_rule="all_success")

    custom_task = BashOperator(task_id='shell_execute', bash_command='echo "Hello World"')

    end = DummyOperator(task_id="end", trigger_rule="all_success")

    start >> custom_task >> end
