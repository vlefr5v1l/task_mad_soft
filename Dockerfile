# Dockerfile для app
FROM python:3.11

WORKDIR /mad_soft

COPY . .

RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary boto3 pytest

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

