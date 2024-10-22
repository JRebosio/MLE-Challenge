# syntax=docker/dockerfile:1.2
FROM python:3.9-slim
# put you docker configuration here

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt


CMD ["uvicorn", "challenge.api:app", "--host", "0.0.0.0", "--port", "8000"]


EXPOSE 8000
