# Python Istio Demo for Kubernetes

This is adapted from a Google IO 18 presentaion.

To build each docker file use the targets (backend, middleware and frontend):
	docker build --target=backend -t backend:latest .

To run all services locally use run_local.sh. The app is available at localhost:8080.

What is the rate of failure for 3 services if each service has a 0.3 probability of failing ?

You add the p(any 1 service fails) plus p(any 2 services fail) plus p(all services fail):

	1(0.3^3) + 3(0.3^2 + 0.7) + 3(0.3 * 0.7^2) =  0.6569999999999999

