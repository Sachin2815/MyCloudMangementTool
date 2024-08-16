#!/usr/bin/python3
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print("Content-type: text/html")
print()
import boto3
import cgi

form=cgi.FieldStorage()
img=form.getvalue("image")
keyname=form.getvalue("keyname")
if (img=="Amazon" or img=="amazon"):
    img="ami-03b31136fc503b84a"
elif (img=="Redhat9" or img=="redhat9"):
    img="ami-008b85aa3ff5c1b02"
elif (img=="ubuntu" or img=="Ubuntu"):
    img="ami-0f5ee92e2d63afc18"
else:
    print("invalid image name")
    pass

ec2=boto3.resource("ec2",aws_access_key_id="",aws_secret_access_key="",region_name='ap-south-1')
createInstance=ec2.create_instances(
        ImageId=img,
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
    )

print("<b> EC2 INSTANCE LAUNCHED ........!</b><br/> ")

print("Instance id is :-", createInstance[0].id)