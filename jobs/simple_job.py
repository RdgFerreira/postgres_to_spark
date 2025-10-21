import os
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import pandas as pd
import dotenv as dtenv

if __name__ == "__main__":
    dtenv.load_dotenv()
    # Initialize Spark Session with PostgreSQL JDBC driver
    spark = SparkSession.builder \
        .appName("PostgreSQL-Spark Connection") \
        .master("spark://spark-master:7077") \
        .config("spark.jars.packages", "org.postgresql:postgresql:42.6.0") \
        .config("spark.executor.memory", "1g") \
        .config("spark.driver.memory", "1g") \
        .config("spark.executor.cores", "1") \
        .config("spark.driver.extraJavaOptions", "-Dlog4j.configuration=file:///opt/spark/conf/log4j.properties") \
        .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
        .config("spark.eventLog.enabled", "true") \
        .config("spark.eventLog.dir", "file:///opt/spark/spark-events") \
        .getOrCreate()

    # Check Spark version
    print(f"Spark version: {spark.version}")

    pg_host = "db"
    pg_port = "5432"
    pg_user = "admin"
    pg_password = os.environ.get("POSTGRES_PASSWORD")
    pg_database = "my_database"

    jdbc_url = f"jdbc:postgresql://{pg_host}:{pg_port}/{pg_database}"

    connection_properties = {
        "user": pg_user,
        "password": pg_password,
        "driver": "org.postgresql.Driver",
        "ssl": "false"
    }

    main_df = spark.read.jdbc(url=jdbc_url, table="ddn_mapa", properties=connection_properties)
    main_df.createOrReplaceTempView("ddn_mapa_view")
    result = spark.sql("""
        SELECT COUNT(*)
        FROM ddn_mapa_view as dmv
        WHERE dmv.vl_tempo_segundos < 1800
    """)

    custom_filename = "query_result.csv"
    os.makedirs("/app/results", exist_ok=True)
    result.toPandas().to_csv(f"/app/results/{custom_filename}", index=False)