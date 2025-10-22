import airflow
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id = "spark_postgres_job",
    default_args = {
        "owner": "airflow",
    },
    start_date=datetime(2024, 1, 1),
    schedule=timedelta(days=1)
)

start = PythonOperator(
    task_id = "start",
    python_callable = lambda: print("Starting Spark Postgres Job DAG"),
    dag = dag,
)

spark_job = SparkSubmitOperator(
    task_id = "spark_postgres_job_task",
    application = "/jobs/simple_job.py",
    conn_id = "spark_conn",
    # application_args = [],
    verbose = True,
    dag = dag,
)

end = PythonOperator(
    task_id="end",
    python_callable = lambda: print("Jobs completed successfully"),
    dag=dag
)

start >> spark_job >> end