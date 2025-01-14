.PHONY: help init install build run test test-api

help:
	@echo "Makefile commands:"
	@echo "  init       Install project dependencies"
	@echo "  install    Install project dependencies (same as init)"
	@echo "  build      Build the Docker image"
	@echo "  run        Run the Flask application"
	@echo "  test       Run the unit tests"
	@echo "  test-api   Test the API endpoints"

init:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Installe les dépendances du projet (synonyme de init)
install: init

# Build l'image Docker
build:
	@echo "Building the Docker image..."
	docker build -t health-calculator-service .

# Lancer l'application Flask
run:
	@echo "Running the Flask app..."
	python app.py

# Exécuter les tests unitaires
test:
	@echo "Running unit tests..."
	python -m unittest test.py
# Tester les endpoints de l'API avec curl (exemple simple)
test-api:
	@echo "Testing API endpoints..."
	curl -X GET http://localhost:5001/health
