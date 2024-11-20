
docker-prune:
	docker compose down                    # Stops containers and removes containers, networks, volumes, and images created by up.
	# docker stop $(docker ps -a -q)       # stop all the containers
	# docker rm $(docker ps -a -q)         # remove all the containers
	docker system prune                    # -a --volumes
	docker-compose up


docker-prune-volumes:
	docker compose down                    # Stops containers and removes containers, networks, volumes, and images created by up.
	# docker stop $(docker ps -a -q)       # stop all the containers
	# docker rm $(docker ps -a -q)         # remove all the containers
	docker system prune -a --volumes
	docker-compose up

bash-lambda:
	docker exec -it stori-lambda bash

bash-db:
	docker exec -it stori-db bash
# psql -h localhost -U postgres

test-local:
	curl "http://localhost:8080/2015-03-31/functions/function/invocations" -d '{}'
	curl "http://localhost:8080/2015-03-31/functions/function/invocations" -d '{"body": "{\"email\":\"ente011@gmail.com\"}"}'


test-deploy:
	curl "${AWS_INVOKE_URL}" --header "Content-Type: application/json" -d '{}'
	curl "${AWS_INVOKE_URL}" --header "Content-Type: application/json" --data-raw '{"emails":"ente011@gmail.com"}'


# https://docs.docker.com/engine/reference/commandline/compose_down/
# https://github.com/NaysanSaran/pandas2postgresql/blob/master/notebooks/Psycopg2_Bulk_Insert_copy_from.ipynb
