#!/bin/bash

docker build --target=microservice-demo -t nshazly/microservice-demo:latest .
docker push nshazly/microservice-demo


