# Dockerfile для media_service
FROM python:3.11

WORKDIR /media_service

COPY src src

RUN pip install fastapi uvicorn boto3

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8001"]
