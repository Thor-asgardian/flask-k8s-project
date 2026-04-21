# Kubernetes Multi-App Deployment

## Components
- App1 (Frontend Flask)
- App2 (Backend Flask)

## Architecture
Client → App1 → App2

## Steps
1. Docker build & push
2. Kubernetes deployment
3. Service exposure

## Scaling
kubectl scale deployment app1 --replicas=3
kubectl scale deployment app2 --replicas=2
