FROM spark:4.0.0-scala2.13-java21-ubuntu
COPY requirements.txt requirements.txt
USER root
RUN set -ex; \
    apt-get update; \
    apt-get install -y python3 python3-pip; \
    rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
RUN mkdir -p /home/spark && \
    chown -R spark:spark /home/spark
USER spark
WORKDIR /app
EXPOSE 8888