# Item Rest API

# Setup
## Prerequisites
    Before using this project, make sure you have the following installed:
    - Docker
    - Make

## Configuration
    This project uses a .env file to store environment variables for the Flask application. Here’s an example of the .env file:

    ```bash
    APP=flask-app
    PORT=8080
    FLASK_ENV=development
    FLASK_DEBUG=1
    ```

You can modify these variables as needed to configure the application.

## Makefile Commands
### make up
    Builds and runs the Flask application in Docker with the environment variables from the .env file.

    ```bash
    make up
    ```
    This will:
    Build the Docker image.
    Run the container in detached mode (-d), mapping port 8080 to the container's internal port 5000.

### make down
    Stops and removes any running containers created by the Flask application.

    ```bash
    make down
    ```
    This will:
    Stop any running container using the flask-app image.
    Remove the stopped container.

### make clean
Cleans up the Docker environment by stopping and removing containers and images associated with the Flask application.

    ```bash
    make clean
    ```
    This will:
    Stop and remove any running containers using the flask-app image.
    Remove the Docker image associated with the Flask application.

### make logs
    Displays the logs of the running Flask container.

    ```bash
    make logs
    ```
    This will:
    Show the logs for the container running the flask-app image.
