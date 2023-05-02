import smtplib 
from email.message import EmailMessage

sender = "sistemaserviciosocialesca@gmail.com" ##CORREO DEL SISTEMA DE ADMINISTRADOR
email_smtp = "smtp.gmail.com" 
email_password = "ptditjjsdwrrxtxs"

def send_email(receiver, subject, content):


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
    
def enviar_correo(email_receiver, email_subject, customText):
    # email_receiver = "jorgecruzmen2000@gmail.com"
    # email_subject = "Expediente aceptado."
    # customText = "carta término"
    content = '''
        <!DOCTYPE html> 
        <head> 
            <meta charset="UTF-8">
        </head>    
            <body style="display: flex; justify-content: center; align-items: center; flex-direction: column; width: max-content; margin: auto;">  
                <div style="margin: auto;">
                    <header style="display: flex; text-align: center; justify-content: space-around; align-items: center;">
                        <div>
                        <img src="https://www.ipn.mx/assets/files/main/img/template/pleca-ipn.png" alt="img">
                        </div>
                    
                        <div>
                        <h2>INSTITUTO POLITÉCNICO NACIONAL</h2>
                        <h3> ESCUELA SUPERIOR DE COMERCIO Y ADMINISTRACIÓN</h3>
                        <h3> UNIDAD SANTO TOMÁS</h3> 
                        </div>
                    
                        <div>
                            <img src="https://www.escasto.ipn.mx/assets/files/main/img/logotipos-UR/ns/ESCA-STO.png" alt="img">
                        </div>
                    
                    </header>
                    <div style="justify-content: center; align-items: center; border-radius: 10px; box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24); padding: 2%;">
                        <h3 style="text-align: center;">Sistema Intrainstitucional de Registro y Seguimiento para Servicio Social ESCA UST</h3>        
                        <p>Buen día, alumno</p>
                        <p>{customText}.</p>
                    </div>
                </div>      
            </body> 
        </html>
    '''.format(customText=customText)
    send_email(email_receiver, email_subject, content)

def enviar_correo_contrasena(email_receiver, email_subject, customText):
    # email_receiver = "jorgecruzmen2000@gmail.com"
    # email_subject = "Expediente aceptado."
    # customText = "carta término"
    content = '''
        <!DOCTYPE html> 
        <head> 
            <meta charset="UTF-8">
        </head>    
            <body style="display: flex; justify-content: center; align-items: center; flex-direction: column; width: max-content; margin: auto;">  
                <div style="margin: auto;">
                    <header style="display: flex; text-align: center; justify-content: space-around; align-items: center;">
                        <div>
                        <img src="https://www.ipn.mx/assets/files/main/img/template/pleca-ipn.png" alt="img">
                        </div>
                    
                        <div>
                        <h2>INSTITUTO POLITÉCNICO NACIONAL</h2>
                        <h3> ESCUELA SUPERIOR DE COMERCIO Y ADMINISTRACIÓN</h3>
                        <h3> UNIDAD SANTO TOMÁS</h3> 
                        </div>
                    
                        <div>
                            <img src="https://www.escasto.ipn.mx/assets/files/main/img/logotipos-UR/ns/ESCA-STO.png" alt="img">
                        </div>
                    
                    </header>
                    <div style="justify-content: center; align-items: center; border-radius: 10px; box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24); padding: 2%;">
                        <h3 style="text-align: center;">Sistema Intrainstitucional de Registro y Seguimiento para Servicio Social ESCA UST</h3>        
                        <p>Buen día, alumno, se ha enviado una solicitud de restablecimiento de contraseña </p>
                        <p>{customText}.</p>
                    </div>
                </div>      
            </body> 
        </html>
    '''.format(customText=customText)
    send_email(email_receiver, email_subject, content)


def enviar_correo_altaAdmin(email_subject, customText):
    # email_receiver = "jorgecruzmen2000@gmail.com"
    # email_subject = "Expediente aceptado."
    # customText = "carta término"
    content = '''
        <!DOCTYPE html> 
        <head> 
            <meta charset="UTF-8">
        </head>    
            <body style="display: flex; justify-content: center; align-items: center; flex-direction: column; width: max-content; margin: auto;">  
                <div style="margin: auto;">
                    <header style="display: flex; text-align: center; justify-content: space-around; align-items: center;">
                        <div>
                        <img src="https://www.ipn.mx/assets/files/main/img/template/pleca-ipn.png" alt="img">
                        </div>
                    
                        <div>
                        <h2>INSTITUTO POLITÉCNICO NACIONAL</h2>
                        <h3> ESCUELA SUPERIOR DE COMERCIO Y ADMINISTRACIÓN</h3>
                        <h3> UNIDAD SANTO TOMÁS</h3> 
                        </div>
                    
                        <div>
                            <img src="https://www.escasto.ipn.mx/assets/files/main/img/logotipos-UR/ns/ESCA-STO.png" alt="img">
                        </div>
                    
                    </header>
                    <div style="justify-content: center; align-items: center; border-radius: 10px; box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24); padding: 2%;">
                        <h3 style="text-align: center;">Sistema Intrainstitucional de Registro y Seguimiento para Servicio Social ESCA UST</h3>        
                        <p>Buen día, se ha recibido la solicitud para dar de alta un nuevo administrador, su código de verificación es </p>
                        <p>{customText}.</p>
                    </div>
                </div>      
            </body> 
        </html>
    '''.format(customText=customText)
    send_email(sender, email_subject, content)