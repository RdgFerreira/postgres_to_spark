up: 
	docker compose up

# 	docker compose down --rmi all
down: 
	docker compose down

build: 
	docker compose build

down_up: 
	docker compose down && docker compose up

clean:
	docker compose down && docker system prune -f && docker image prune -f && docker volume prune -f

dev: 
	docker exec -it spark-master bash

run-scaled: 
	make down && docker-compose up --scale spark-worker=3

stop: 
	docker-compose stop

submit: 
	docker exec spark-master spark-submit --master spark://spark-master:7077 --deploy-mode client ./apps/$(app)