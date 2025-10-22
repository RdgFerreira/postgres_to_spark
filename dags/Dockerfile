FROM apache/airflow:latest-python3.13
USER root
COPY requirements.txt requirements.txt
RUN apt-get update && \
    apt-get install -y gcc python3-dev openjdk-17-jdk && \
    apt-get clean
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
USER airflow
RUN pip install -r requirements.txt