import smtplib
import time
from email.message import EmailMessage
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
import ssl



name = 'sender_name '
address_sender = 'sender_email '
password_sender = "password"
input_address_recipients = 'recipient_email '
address_recipients = input_address_recipients.split(',')
subject = 'automated email '
body = 'welcome to automated email '

email_msg = EmailMessage()

email_msg['From'] = address_sender
email_msg['To'] = ','.join(input_address_recipients)
email_msg['Subject'] = subject
email_msg.set_content(body)

#create a default connection if its taking time to send bulk message
context = ssl.create_default_context()

def perform_task():
   


 with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as mysmtp:
    mysmtp.login(address_sender,password_sender)
    mysmtp.sendmail(address_sender,input_address_recipients, email_msg.as_string())
    print('Hi message sent successfully to all cohorts')

while True:
    perform_task()
    time.sleep(5)

   
   

      
