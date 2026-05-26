import smtplib
from email.message import EmailMessage

class SMTPMail:
    
    #Construtor da classe
    def __init__(self, senderEmail, password):
        self.email = senderEmail
        self.password = password

    #Metodo para envio do email
    def sendEmail(self, destiny):
        
        ##Criando objeto da mensagem
        msg = EmailMessage()
        msg['Subject'] = 'Envio de SMTP Python'
        msg['From'] = self.email
        msg['To'] = destiny
        msg.set_content('Corpo do email de teste a ser enviado via python.')         

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email, self.password)
                smtp.send_message(msg)
            print("Email enviado com sucesso!\n Verifique sua caixa de email")
        
        except Exception as e:
            print(f"Erro ao enviar email: \n {e}")

