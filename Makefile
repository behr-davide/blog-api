build:
		docker-compose build

up: 
		docker-compose up -d blog postgres

test: up
		docker-compose run --rm --no-deps --entrypoint=pytest blog /tests

down:
		docker-compose down --remove-orphans

reload: down build up

all: down build up test