'''
import smtplib
from email.mime.text import MIMEText

def send_email(to, subject, body, gmail_user,gmail_pass):
    msg=MIMEText(body)
    msg['Subject'] = subject; msg['From']=gmail_user; msg['To']=to
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as s:
        s.login(gmail_user, gmail_pass,); s.send_message(msg); print('Email Sent!')'''

import smtplib
from email.mime.text import MIMEText

def send_email(to, subject, body, gmail_user, gmail_pass):
    
    msg = MIMEText(body)
    
    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = to

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as s:
        s.login(gmail_user, gmail_pass)
        s.send_message(msg)

    print("Email Sent!")

# Example
send_email(
    "ashimacharyaa08@gmail.com",
    "Test Email",
    "Hello from Python!",
    "acharyaashim13@gmail.com",
    "aashikaacharya"
)