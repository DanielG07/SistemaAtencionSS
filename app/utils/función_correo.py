import smtplib 
from email.message import EmailMessage

def send_email(receiver, subject, content):

    sender = "enda0507@gmail.com" ##CORREO DEL SISTEMA DE ADMINISTRADOR

    email_smtp = "smtp.gmail.com" 
    email_password = "nkjvhfykxxtbuykb" 

    # Create an email message object 
    message = EmailMessage() 

    # Configure email headers 
    message['Subject'] = subject 
    message['From'] = sender 
    message['To'] = receiver

    # Add message content as html type
    message.set_content(content, subtype='html')

    # Set smtp server and port 
    server = smtplib.SMTP(email_smtp, '587') 

    # Identify this client to the SMTP server 
    server.ehlo() 

    # Secure the SMTP connection 
    server.starttls() 

    # Login to email account 
    server.login(sender, email_password) 

    # Send email 
    server.send_message(message) 

    # Close connection to server 
    server.quit()
    
def main():
    receiver_email_address = "jorgecruzmen2000@gmail.com"
    email_subject = "Email test from Python"
    with open('./app/message.html', 'r') as file:
        file_content = file.read()
    send_email(receiver_email_address, email_subject, file_content)

if __name__ == '__main__':
    main()
