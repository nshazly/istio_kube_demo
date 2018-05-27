# Python Istio Demo for Kubernetes

This is adapted from a Google IO 18 presentaion.

To build each docker file use the targets (backend, middleware and frontend):
	docker build --target=backend -t backend:latest .

To run all services locally use run_local.sh. The app is available at localhost:8080.

What is the rate of failure for 3 services if each ahs a 0.3 probability of failing ?

You add the probabliities of any 1 service failing plus any 2 services failing and all services failing:

	1(0.3^3) + 3(0.3^2 + 0.7) + 3(0.3 * 0.7^2) =  0.6569999999999999

