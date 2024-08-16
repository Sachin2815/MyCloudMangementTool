#!/usr/bin/python3
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print("Content-type: text/html")
print()
import boto3
import cgi

form=cgi.FieldStorage()
size=form.getvalue("size")
zone=form.getvalue("zone")
access_key = ''
secret_key = ''
region = 'ap-south-1'
ec2_client = boto3.client(
    'ec2',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region
    )
response = ec2_client.create_volume(
    AvailabilityZone=zone,
    Size=int(size)
    )
volume_id = response['VolumeId']
print("<b>EBS Volume of size </b>"+ size + " <b>has been launched in zone </b>"+zone)
print("<br/><b>Volume ID:</b>",volume_id)