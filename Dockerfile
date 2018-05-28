FROM python:3 as base

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]

FROM base as microservice-demo
CMD ["backend.py"]

