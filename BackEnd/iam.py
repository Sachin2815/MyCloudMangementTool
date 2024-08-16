#!/usr/bin/python3
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print("Content-type: text/html")
print()
import boto3
import cgi

form=cgi.FieldStorage()
name=form.getvalue("name")
access_key = ''
secret_key = ''

session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='ap-south-1'
)

iam_client = session.client('iam')

username = name  # Replace with your desired IAM username

response = iam_client.create_user(
    UserName=username
)

print(f"IAM user '{username}' created successfully!")