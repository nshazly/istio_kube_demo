# Python Istio Demo for Kubernetes

This repo contains an example of a microservices deployment for kubernetes (frontend/middleware/backend) with Istio sidecars.

Prerequisites:
    1. You have a running cluster
    2. Istio is already installed in the cluster
    
This is adapted from a Google IO 18 presentaion.

To build the general purpose docker file run
	
    docker build --target=microservice-demo -t microservice-demo:latest .

You can use build.sh to build and push your image to your private repo, update the values in the file.

To run all services locally use run_local.sh. The app is available at localhost:8080.

To deploy to kubernetes run:
    
    kubectl apply -f manifest.yaml --namespace=istio-demo

This will create 3 deployments and services. The frontend service will provision a load balancer with an external IP address.

    # to display the external ip address
    kubectl get svc frontend-service

What is the rate of failure for 3 services if each ahs a 0.3 probability of failing ?

You add the probabliities of any 1 service failing plus any 2 services failing and all services failing:

	1(0.3^3) + 3(0.3^2 + 0.7) + 3(0.3 * 0.7^2) =  0.6569999999999999

