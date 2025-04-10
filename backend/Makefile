.PHONY: setup run test clean lint format mock

# Variables
VENV = venv
PYTHON = python3
PIP = $(VENV)/bin/pip
SRC_DIR = src
MOCK_DIR = mock

# Default target
all: setup

# Setup virtual environment and install dependencies
setup:
	@echo "Setting up virtual environment..."
	python -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "Setup complete!"

# Run the application
run:
	@echo "Starting the application..."
	@uvicorn $(SRC_DIR).api:app --reload --port 9000

# Run mock server
mock:
	@echo "Starting the mock server..."
	@uvicorn $(MOCK_DIR).main:app --reload --port 9000

# Run tests
test:
	@echo "Running tests..."
	$(PYTHON) -m pytest

venv:
	@echo "Creating virtual environment..."
	$(PYTHON) -m venv $(VENV)
	@echo "Installing dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

install:
	@echo "Installing dependencies..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Clean up generated files
clean:
	@echo "Cleaning up..."
	rm -rf __pycache__
	rm -rf $(SRC_DIR)/__pycache__
	rm -rf $(MOCK_DIR)/__pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +

# Lint the code
lint:
	@echo "Running linter..."
	$(PYTHON) -m flake8 $(SRC_DIR) $(MOCK_DIR)

# Format the code
format:
	@echo "Formatting code..."
	$(PYTHON) -m black $(SRC_DIR) $(MOCK_DIR)
	$(PYTHON) -m isort $(SRC_DIR) $(MOCK_DIR)

# Help command
help:
	@echo "Available commands:"
	@echo "  make setup    - Set up virtual environment and install dependencies"
	@echo "  make run      - Run the application"
	@echo "  make mock     - Run the mock server"
	@echo "  make test     - Run tests"
	@echo "  make clean    - Clean up generated files"
	@echo "  make lint     - Run linter"
	@echo "  make format   - Format code"
	@echo "  make help     - Show this help message"
