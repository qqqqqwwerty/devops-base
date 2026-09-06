#!/bin/bash

# Kubernetes deployment script for devops-base project

NAMESPACE="devops-base"

echo "Creating namespace..."
kubectl apply -f k8s/namespace.yaml

echo "Creating ConfigMaps and Secrets..."
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/nginx-configmap.yaml
kubectl apply -f k8s/secret.yaml

echo "Deploying PostgreSQL StatefulSet..."
kubectl apply -f k8s/postgres-statefulset.yaml

echo "Creating Services..."
kubectl apply -f k8s/postgres-service.yaml
kubectl apply -f k8s/backend-service.yaml
kubectl apply -f k8s/nginx-service.yaml

echo "Deploying backend and nginx..."
kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/nginx-deployment.yaml

echo "Creating Ingress..."
kubectl apply -f k8s/ingress.yaml

echo "Waiting for deployments to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/backend -n $NAMESPACE
kubectl wait --for=condition=available --timeout=300s deployment/nginx -n $NAMESPACE
kubectl wait --for=condition=ready --timeout=300s pod/postgres-0 -n $NAMESPACE

echo "Deployment completed!"
echo "Pods status:"
kubectl get pods -n $NAMESPACE
echo "Services status:"
kubectl get services -n $NAMESPACE
echo "Ingress status:"
kubectl get ingress -n $NAMESPACE