# FROM apache/airflow:latest-python3.11
# FROM python:3.11.14-trixie
# USER root
# RUN set -ex; \
#     apt-get update; \
#     apt-get install -y gcc python3 python3-dev python3-pip openjdk-17-jdk; \
#     rm -rf /var/lib/apt/lists/*
# USER airflow
# RUN pip install --no-cache-dir "apache-airflow[postgres,spark,fab]==2.7.3" psycopg2-binary pyspark==4.0.0
# ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
# ENV AIRFLOW_HOME=/opt/airflow
# WORKDIR ${AIRFLOW_HOME}
# ENTRYPOINT ["/entrypoint.sh"]
# COPY requirements.txt requirements.txt
# USER airflow
# RUN pip install -r requirements.txt
# USER root



FROM apache/airflow:latest-python3.13

USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends default-jdk && \
    apt-get install -y --no-install-recommends wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER airflow
RUN pip install pyspark==4.0.0
RUN pip install apache-airflow-providers-apache-spark

ENV JAVA_HOME=/usr/lib/jvm/default-java
ENV AIRFLOW_HOME=/opt/airflow
ENV PYTHONPATH=${AIRFLOW_HOME}/dags:${PYTHONPATH}
WORKDIR ${AIRFLOW_HOME}
# RUN wget https://jdbc.postgresql.org/download/postgresql-42.7.8.jar -O /opt/spark/jars/postgresql-42.7.8.jar

USER airflow
EXPOSE 8793
