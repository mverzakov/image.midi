.DEFAULT_GOAL := test

DJANGO_ROOT = ./src
MANAGE = cd $(DJANGO_ROOT) && python manage.py
DOCKER = docker
DOCKER_COMPOSE = docker-compose

clean:
	docker-compose stop
	docker-compose rm --all --force
	rm -rf $(DJANGO_ROOT)/static
	rm -rf .docker
	rm -rf .tox

collectstatic:
	$(MANAGE) collectstatic --noinput

migrate:
	$(MANAGE) migrate --noinput

start:
	docker-compose up