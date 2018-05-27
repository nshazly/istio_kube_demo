FROM python:3 as base

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["env python", "main.py"]

FROM base as backend
ENTRYPOINT  ["env python","backend.py"]

FROM base as frontend
ENTRYPOINT ["env python", "frontend.py"]

FROM base as middleware
ENTRYPOINT ["env python", "middleware.py"]


