up: 
	docker compose up

down: 
	docker compose down

build: 
	docker compose build

down_up: 
	docker compose down && docker compose up

clean:
	docker compose down && docker system prune -f && docker image prune -f && docker volume prune -f

clean_delete_volumes:
	docker compose down -v && docker system prune -f && docker image prune -f && docker volume prune -f

clean_restart:
	make clean && make up

clean_build_restart: 
	make clean && make build && make clean && make up

clean_all_volumes_restart: 
	make clean_delete_volumes && make clean_restart


remove_all_volumes:
	docker volume rm $(docker volume ls -qf dangling=true)

dev: 
	docker exec -it spark-master bash

run-scaled: 
	make down && docker-compose up --scale spark-worker=3

stop: 
	docker-compose stop

# submit single job to spark cluster
# usage: make submit app=<path/to/app_file.py>
submit: 
	docker exec spark_master spark-submit --master spark://spark-master:7077 --deploy-mode client ./$(app)

# Inside scheduler: airflow dags reserialize to visualize errors in dag python files
# docker exec scheduler airflow dags reserialize