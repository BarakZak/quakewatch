QuakeWatch
A Flask application for earthquake monitoring, deployed with Kubernetes and Helm.
Project Structure

app.py: Flask app with / and /health endpoints.
Dockerfile: Builds barakzak/quakewatch image.
helm/quakewatch/: Helm chart for deployment.
tests/test_app.py: Unit tests for Flask endpoints.
.github/workflows/ci-cd.yml: GitHub Actions CI/CD pipeline.

CI/CD Pipeline

GitHub Actions workflow builds, tests, and deploys the app.
Tests run across Python 3.8, 3.9, 3.10 with pytest.
Pushes Docker image to barakzak/quakewatch and deploys Helm chart to Docker Desktop Kubernetes.

Helm Chart Publishing
The Helm chart is published to a ChartMuseum repository.
Setup ChartMuseum
docker run --rm -it -p 8080:8080 -e STORAGE=local -e STORAGE_LOCAL_ROOTDIR=/charts -v %CD%\chartmuseum-storage:/charts ghcr.io/helm/chartmuseum:v0.16.1

Package and Publish
helm package ./helm/quakewatch
curl --data-binary "@quakewatch-0.1.1.tgz" http://localhost:8080/api/charts

Install Chart
helm repo add chartmuseum http://localhost:8080
helm repo update
helm install quakewatch chartmuseum/quakewatch --namespace default

