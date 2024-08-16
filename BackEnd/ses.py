#!/usr/bin/python3
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print('Content-Type: text/html')
print()
import boto3
import uuid
import cgi

access_key = ''
secret_key = ''

session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='ap-south-1'
)

s3_client = session.client('s3')

myuuid = uuid.uuid1().int

form = cgi.FieldStorage()
user_email = form.getvalue('email')
user_subject = form.getvalue('subject')
user_message = form.getvalue('message')

response = s3_client.put_object(
    Bucket = 'emailbucket1006',
    Key = 'myemaillist.txt'+str(myuuid),
    Body = user_email
)

data = s3_client.get_object(
    Bucket = 'emailbucket1006',
    Key = 'myemaillist.txt'+str(myuuid)
)

emailstr = data["Body"].read().decode('utf-8')
emaillist = emailstr.split(",")

ses_client = session.client("ses")

res = ses_client.send_email(
    Source='agrawalprerit780@gmail.com',
    Destination={
        'ToAddresses': emaillist,
    },
    Message={
        'Subject': {
            'Data': user_subject,
            'Charset': 'UTF-8'
        },
        'Body': {
            'Text': {
                'Data': user_message,
                'Charset': 'UTF-8'
            },
        }
    }
)
print(res)