#!/usr/bin/python3
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print("Content-type: text/html")
print()
import boto3
import cgi

form=cgi.FieldStorage()
instance_id=form.getvalue("instance_id")
volume_id=form.getvalue("volume_id")

access_key = ''
secret_key = ''

session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)

ec2_client = session.client('ec2',region_name='ap-south-1')

response = ec2_client.attach_volume(
    Device='/dev/xvdf', 
    InstanceId=instance_id,
    VolumeId=volume_id
)
print(response)