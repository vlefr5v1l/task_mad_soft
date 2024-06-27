# Dockerfile.media_service для app
FROM python:3.11

WORKDIR /app

COPY app /app/app

RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary boto3

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
