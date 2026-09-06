#!/bin/bash

# Kubernetes cleanup script for devops-base project

NAMESPACE="devops-base"

echo "Deleting Kubernetes resources in namespace $NAMESPACE..."

kubectl delete -f k8s/ingress.yaml --ignore-not-found=true
kubectl delete -f k8s/nginx-deployment.yaml --ignore-not-found=true
kubectl delete -f k8s/backend-deployment.yaml --ignore-not-found=true
kubectl delete -f k8s/postgres-statefulset.yaml --ignore-not-found=true
kubectl delete -f k8s/nginx-service.yaml --ignore-not-found=true
kubectl delete -f k8s/backend-service.yaml --ignore-not-found=true
kubectl delete -f k8s/postgres-service.yaml --ignore-not-found=true
kubectl delete -f k8s/nginx-configmap.yaml --ignore-not-found=true
kubectl delete -f k8s/configmap.yaml --ignore-not-found=true
kubectl delete -f k8s/secret.yaml --ignore-not-found=true
kubectl delete -f k8s/namespace.yaml --ignore-not-found=true

echo "Cleanup completed!"
echo "Remaining resources (if any):"
kubectl get all -n $NAMESPACE --ignore-not-found=true