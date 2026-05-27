import smtplib
from email.message import EmailMessage
from datetime import date

class SMTPMail:
    
    #Construtor da classe
    def __init__(self, email, password):
        self.email = email
        self.password = password

    #Metodo para envio do email de Status dos processos
    def status_email(self, subject, destiny, process="", sterror=0, logerror=""):
        
        if(sterror == 0):
            diaEnv = self.get_formated_date()
            ##Criando objeto da mensagem de SUCESSO
            msg = EmailMessage()
            msg['Subject'] = diaEnv +  subject
            msg['From'] = self.email
            msg['To'] = destiny
            msg.set_content('Sucesso ao realizar ' + process + ' no dia ' + self.get_formated_date())         

            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(self.email, self.password)
                    smtp.send_message(msg)
                print(f"EMAIL ENVIADO COM SUCESSO\n Destinatário: {destiny}")

            except Exception as e:
                print(f"FALHA NO ENVIO DE EMAIL\n\n Destinatário: {destiny} \n Erro:\n {e}")
        else:
            diaEnv = self.get_formated_date()
            ##Criando objeto da mensagem de SUCESSO
            msg = EmailMessage()
            msg['Subject'] = diaEnv +  subject
            msg['From'] = self.email
            msg['To'] = destiny
            msg.set_content('FALHA ao realizar ' + process + ' no dia ' + self.get_formated_date() + '\n ' + logerror)         

            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(self.email, self.password)
                    smtp.send_message(msg)
                print(f"EMAIL ENVIADO COM SUCESSO\n Destinatário: {destiny}")

            except Exception as e:
                print(f"FALHA NO ENVIO DE EMAIL\n\n Destinatário: {destiny} \n Erro:\n {e}")
        

    def get_formated_date(self):
        hoje = date.today()
        return hoje.strftime('%d/%m/%Y')