import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
        dag_id='my_dag',
        start_date = datetime.datetime(2024,1,1),
        schedule='@once',
        ):
        EmptyOperator(task_id='task')
