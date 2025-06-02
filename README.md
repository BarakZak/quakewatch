QuakeWatch is a Flask-based web application designed to display real-time and historical earthquake data. It fetches data from external APIs and presents it in an easy-to-understand format.

## Features

- Real-time earthquake data visualization
- Historical earthquake data lookup
- Interactive map integration
- Customizable alerts and notifications

## Running the Containerized Version

To run the containerized version of QuakeWatch, follow these steps:

### Prerequisites

- Ensure you have [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.

### Cloning the Repository

1. Clone the repository:
   ```bash
   git clone https://github.com/EduardUsatchev/QuakeWatch.git
   cd QuakeWatch
   ```

### Building the Docker Image

2. Build the Docker image using the following command:
   ```bash
   docker build -t quakewatch:latest .
   ```

### Running the Docker Container

3. Run the container using Docker Compose:
   ```bash
   docker-compose up -d
   ```
   The application will be accessible at `http://localhost:5000`.

### Stopping the Container

4. To stop the container, use:
   ```bash
   docker-compose down
   ```

## Pushing to Docker Hub

To push the built image to Docker Hub, follow these steps:

1. Build and tag the image:
   ```bash
   docker build -t your_dockerhub_username/quakewatch:latest .
   ```
2. Log in to Docker Hub:
   ```bash
   docker login
   ```
3. Push the image:
   ```bash
   docker push your_dockerhub_username/quakewatch:latest
   ```

Replace `your_dockerhub_username` with your actual Docker Hub username.