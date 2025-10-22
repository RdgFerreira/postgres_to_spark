import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id = "spark_postgres_job",
    default_args = {
        "owner": "airflow",
        "start_date": airflow.utils.dates.days_ago(1),
    },
    schedule_interval = None,
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