#!/usr/bin/python3
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print("Content-type: text/html")
print()

import cgi

form=cgi.FieldStorage()
receiver_number=form.getvalue("number")
message=form.getvalue("message")

number="+91"+receiver_number

from twilio.rest import Client
# Your Account Sid and Auth Token from twilio account
account_sid = ''
auth_token = ''
# instantiating the Client
client = Client(account_sid, auth_token)
messagesent = client.messages.create(body=message, from_='', to=number)
print("Message Successfully sent and the message id is",messagesent.sid)