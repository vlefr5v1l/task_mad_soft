import boto3
from botocore.client import Config

S3_ENDPOINT_URL = "http://minio:9000"
S3_ACCESS_KEY = "minioadmin"
S3_SECRET_KEY = "minioadmin"
S3_BUCKET_NAME = "memes"

s3 = boto3.client('s3',
                  endpoint_url=S3_ENDPOINT_URL,
                  aws_access_key_id=S3_ACCESS_KEY,
                  aws_secret_access_key=S3_SECRET_KEY,
                  config=Config(signature_version='s3v4'))

def upload_file(file, filename):
    s3.upload_fileobj(file, S3_BUCKET_NAME, filename)
    return f"{S3_ENDPOINT_URL}/{S3_BUCKET_NAME}/{filename}"

def delete_file(filename):
    s3.delete_object(Bucket=S3_BUCKET_NAME, Key=filename)
