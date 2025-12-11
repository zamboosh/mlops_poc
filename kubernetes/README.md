# Kubernetes Deployment Guide for HF Sentiment Analysis

This directory contains the Kubernetes manifests to deploy the Sentiment Analysis API.

## Prerequisites

1.  **Kubernetes Cluster**: You need a running cluster. 
    *   For local development: [Docker Desktop](https://docs.docker.com/desktop/kubernetes/), [Minikube](https://minikube.sigs.k8s.io/), or [Kind](https://kind.sigs.k8s.io/).
    *   `kubectl` command-line tool installed and configured.

2.  **Docker Image**: Ensure your image is built and pushed to a registry (or available locally).
    *   The deployment expects the image: `<YOUR_DOCKER_USERNAME>/hf-sentiment-api-fixed:latest`
    *   **Action Required**: Open `deployment.yaml` and update the `image` field with your actual username.

## Deployment Steps

### 1. Update Configuration
Open `kubernetes/deployment.yaml` and locate the `image` field. Replace `<YOUR_DOCKER_USERNAME>` with your Docker Hub username.

```yaml
image: motizamir/hf-sentiment-api-fixed:latest # Example
```

### 2. Apply Manifests
Apply the configuration files to your cluster:

```bash
# Apply Deployment and Service
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml

# (Optional) Apply Ingress if you have an Ingress Controller
kubectl apply -f kubernetes/ingress.yaml
```

### 3. Verify Deployment
Check the status of your pods and services:

```bash
kubectl get pods
kubectl get services
```

Wait until the pod status is `Running` and the `READY` column shows `1/1`.

## Accessing the Application

### Method A: Port Forwarding (Easiest for testing)
To access the service locally without an Ingress controller, use `kubectl port-forward` to map both ports:

```bash
kubectl port-forward service/hf-sentiment-service 8080:8080 8000:8000
```
Now, you can access the application:

- **Frontend**: http://localhost:8000/
- **Predict Endpoint**: http://localhost:8080/predict
- **Health Check**: http://localhost:8080/health

### Method B: Using Ingress
If you deployed the Ingress resource:
1.  Ensure you have an Ingress Controller (like NGINX) running.
2.  Add the following line to your `/etc/hosts` file (need sudo):
    ```
    127.0.0.1 sentiment.local
    ```
3.  Access via `http://sentiment.local/`.
