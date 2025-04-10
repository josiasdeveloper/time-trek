.PHONY: setup install run build test lint clean help

# Variables
NPM = npm
NG = npx ng

# Default target
all: setup

# Setup the project
setup:
	@echo "Setting up the project..."
	$(NPM) install
	@echo "Setup complete!"

# Install dependencies
install:
	@echo "Installing dependencies..."
	$(NPM) install

# Run the development server
run:
	@echo "Starting development server..."
	$(NG) serve

# Build the project
build:
	@echo "Building the project..."
	$(NG) build

# Run tests
test:
	@echo "Running tests..."
	$(NG) test

# Run linting
lint:
	@echo "Running linting..."
	$(NG) lint

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -rf dist/
	rm -rf node_modules/
	rm -rf .angular/

# Help command
help:
	@echo "Available commands:"
	@echo "  make setup    - Set up the project and install dependencies"
	@echo "  make install  - Install dependencies"
	@echo "  make run      - Run the development server"
	@echo "  make build    - Build the project"
	@echo "  make test     - Run tests"
	@echo "  make lint     - Run linting"
	@echo "  make clean    - Clean build artifacts"
	@echo "  make help     - Show this help message"
