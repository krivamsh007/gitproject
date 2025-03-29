
---

### 5. `dags/example_dag.py`

A simple Airflow DAG to kick off a Spark job. (You may need to adapt it based on your Spark setup.)

```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 3, 28),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'spark_job_example',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
)

spark_job = BashOperator(
    task_id='run_spark_job',
    bash_command='spark-submit --master spark://spark-master:7077 /path/to/your/spark_script.py',
    dag=dag,
)

spark_job
