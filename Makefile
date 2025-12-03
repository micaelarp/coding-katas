.PHONY: test rotate build env-start env-stop env-restart env-destroy env-recreate env-reset destroy-containers docker-cleanup _guard-docker

DOCKER_COMMAND = docker-compose

# Ejecuta los tests dentro del contenedor
# Uso: make test
# Si no usas Docker, puedes cambiar la línea a 'pytest .'
test: ## Run test suite in project's main container
	$(DOCKER_COMMAND) exec -T app pytest .

# Ejecuta el script de rotación pasando el mensaje como argumento
# Uso: make rotate "Refactorizado X"
rotate: ## Run tests and commit rotation (Usage: make rotate "Refactored X")
	bash python/scripts/pp_rotate.sh "$(filter-out $@,$(MAKECMDGOALS))"

# Docker management
build: _guard-docker ## Build project image
	$(DOCKER_COMMAND) build --no-cache

env-start: _guard-docker ## Start project containers defined in docker-compose
	$(DOCKER_COMMAND) up -d

env-stop: _guard-docker ## Stop project containers defined in docker-compose
	$(DOCKER_COMMAND) stop

env-restart: env-stop env-start ## Restart project containers defined in docker-compose

env-destroy: _guard-docker ## Destroy all project containers
	$(DOCKER_COMMAND) down -v --rmi all --remove-orphans

env-recreate: build env-start ## Force building project image and start all containers again

env-reset: destroy-containers env-start ## Destroy project containers and start them again

destroy-containers: _guard-docker ## Destroy project containers
	$(DOCKER_COMMAND) down -v

docker-cleanup: _guard-docker ## Purge all Docker images in the system
	$(DOCKER_COMMAND) down -v
	docker system prune -f

_guard-docker:
	@command -v docker >/dev/null 2>&1 || { echo >&2 "Docker no está instalado. Abortando."; exit 1; }
