import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

with DAG("spark_postgres_job",
          default_args={
              "owner": "airflow",
              "depends_on_past": False,
          },
          start_date=datetime(2024, 1, 1),
          schedule=timedelta(days=1)) as dag:
    
    spark_job = SparkSubmitOperator(
        task_id="spark_postgres_job_task",
        application="/app/simple_job.py", # app or jobs/simple_job.py if deployed as external client
        conn_id="spark_default",
        total_executor_cores=1,
        executor_cores=1,
        executor_memory="1g",
        num_executors=1,
        driver_memory="1g",
        verbose=True,
    )

spark_job