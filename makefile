up: 
	docker compose up

# 	docker compose down --rmi all
down: 
	docker compose down

down_up: 
	docker compose down && docker compose up

dev: 
	docker exec -it spark-master bash

run-scaled: 
	make down && docker-compose up --scale spark-worker=3

stop: 
	docker-compose stop

submit: 
	docker exec spark-master spark-submit --master spark://spark-master:7077 --deploy-mode client ./apps/$(app)