#!/usr/bin/python3
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print("Content-type: text/html")
print()
import boto3
import cgi

form=cgi.FieldStorage()
subject=form.getvalue("subject")
msg=form.getvalue("message")

access_key = ''
secret_key = ''

session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='ap-south-1'
)

sns_client = session.client('sns')

response = sns_client.publish(
    TopicArn='',
    Message=msg,
    Subject=subject,
)

print("Email sent successfully and the message id is :",response['MessageId'])