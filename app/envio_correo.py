
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# username = "enda0507@gmail.com"
# password = "nkjvhfykxxtbuykb"
# mail_from = "enda0507@gmail.com"
# mail_to = "jorgecruzmen2000@gmail.com"
# mail_subject = "Test Subject"
# mail_body = "This is a test message"

# mimemsg = MIMEMultipart()
# mimemsg['From']=mail_from
# mimemsg['To']=mail_to
# mimemsg['Subject']=mail_subject
# mimemsg.attach(MIMEText(mail_body, 'plain'))
# connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
# connection.starttls()
# connection.login(username,password)
# connection.send_message(mimemsg)
# connection.quit()

import smtplib 
from email.message import EmailMessage 

email_subject = "Email test from Python" 
sender_email_address = "enda0507@gmail.com" 
receiver_email_address = "jorgecruzmen2000@gmail.com" 
email_smtp = "smtp.gmail.com" 
email_password = "nkjvhfykxxtbuykb" 

# Create an email message object 
message = EmailMessage() 

# Configure email headers 
message['Subject'] = email_subject 
message['From'] = sender_email_address 
message['To'] = receiver_email_address 

with open('./app/message.html', 'r') as file:
   file_content = file.read()

# Add message content as html type
message.set_content(file_content, subtype='html')

# Set smtp server and port 
server = smtplib.SMTP(email_smtp, '587') 

# Identify this client to the SMTP server 
server.ehlo() 

# Secure the SMTP connection 
server.starttls() 

# Login to email account 
server.login(sender_email_address, email_password) 

# Send email 
server.send_message(message) 

# Close connection to server 
server.quit()