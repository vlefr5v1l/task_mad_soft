import boto3
from botocore.client import Config
from botocore.exceptions import ClientError

S3_ENDPOINT_URL = "http://minio:9000"
S3_ACCESS_KEY = "minioadmin"
S3_SECRET_KEY = "minioadmin"
S3_BUCKET_NAME = "memes"

s3 = boto3.client('s3',
                  endpoint_url=S3_ENDPOINT_URL,
                  aws_access_key_id=S3_ACCESS_KEY,
                  aws_secret_access_key=S3_SECRET_KEY,
                  config=Config(signature_version='s3v4'))


def ensure_bucket_exists():
    try:
        s3.head_bucket(Bucket=S3_BUCKET_NAME)
    except ClientError:
        # Если бакет не существует, создаем его
        s3.create_bucket(Bucket=S3_BUCKET_NAME)


def upload_file(file, filename):
    ensure_bucket_exists()
    s3.upload_fileobj(file, S3_BUCKET_NAME, filename)
    return f"{S3_ENDPOINT_URL}/{S3_BUCKET_NAME}/{filename}"


def create_image_url(image_name):
    ensure_bucket_exists()
    s3.upload_fileobj(file, S3_BUCKET_NAME, filename)
    return f"{S3_ENDPOINT_URL}/{S3_BUCKET_NAME}/{filename}"


def delete_file(filename):
    s3.delete_object(Bucket=S3_BUCKET_NAME, Key=filename)
