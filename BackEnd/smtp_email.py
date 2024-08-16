#!/usr/bin/python3
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print("Content-type: text/html")
print()

import cgi
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


form=cgi.FieldStorage()
receiver_email=form.getvalue("receiver_email")
subject=form.getvalue("subject")
body=form.getvalue("body")

def send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create a multipart message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Add body to the email
    msg.attach(MIMEText(message, "plain"))

    try:
        # Create a secure SSL/TLS connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()
        server.ehlo()

        # Login to the SMTP server
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # Close the SMTP connection
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email. Error:", str(e))

sender_email = ""
smtp_server = ""
smtp_port = 587
smtp_username = ""
smtp_password = ""
send_email(sender_email,receiver_email,subject,body,smtp_server,smtp_port,smtp_username,smtp_password)