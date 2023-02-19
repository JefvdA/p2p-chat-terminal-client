.DEFAULT_GOAL := help

build: ## Build the docker containers used in docker compose
	@docker compose build

up: ## Create and run all docker instances in the background with docker compose
	@docker compose up -d

down: ## Stop and remove all docker instances
	@docker compose down

bash: ## Open a bash in the main docker instance
	@docker-compose run --rm main bash

test: ## Run all tests and generate coverage report
	@coverage run -m unittest discover src/tests

coverage: ## Display the coverage report in the terminal
	@coverage report

coverage-html: ## Generate html to show coverage report
	@coverage html

.PHONY: help
help: ## Show this help menu
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
