FROM spark:4.0.0-scala2.13-java21-ubuntu
COPY requirements.txt requirements.txt
USER root
RUN set -ex; \
    apt-get update; \
    apt-get install -y python3 python3-pip openjdk-21-jdk; \
    rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
RUN wget https://jdbc.postgresql.org/download/postgresql-42.7.8.jar -O /opt/spark/jars/postgresql-42.7.8.jar
RUN mkdir -p /home/spark && \
    chown -R spark:spark /home/spark
# USER spark
# RUN chmod u+x /opt/spark/sbin/* && \
#     chmod u+x /opt/spark/bin/*
WORKDIR /app
EXPOSE 8888