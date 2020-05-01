from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import pendulum

default_args = {
        'owner': 'aviandito',
	'start_date': pendulum.datetime(year=2020, month=5, day=1, tzinfo='Asia/Jakarta')
        }

dag = DAG('olx_crawler', 
	default_args=default_args, 
	schedule_interval='0 * * * *', 
	)

t1 = BashOperator(
    task_id='scrape_rumah',
    bash_command="cd ~/olx_crawler && python3 olx_scrape_rumah.py",
    dag=dag,
    retries=3
    )

t2 = BashOperator(
    task_id='scrape_mobkas',
    bash_command="cd ~/olx_crawler && python3 olx_scrape_mobkas.py",
    dag=dag,
    retries=3
    )

t2.set_upstream(t1)
