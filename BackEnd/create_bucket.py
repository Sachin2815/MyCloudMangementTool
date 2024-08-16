#!/usr/bin/python3
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print("Content-type: text/html")
print()
import boto3
import cgi

form=cgi.FieldStorage()
name=form.getvalue("bucket_name")
access_key = ''
secret_key = ''

region = 'ap-south-1'  # Replace with your desired region

# Create an S3 client using access keys
s3_client = boto3.client(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region
)

# S3 bucket name
bucket_name = 'bucket89484-' + name
# Create an S3 bucket
s3_client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': region
    }
)

# Print the bucket creation confirmation
print(f"Bucket '{bucket_name}' created successfully.")