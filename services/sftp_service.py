import paramiko
import os
from services.emailSmtp import SMTPMail

class SFTPService: 

    #Construtor da classe
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
    

    #Metodo para conexão e envio de arquivos
    def transport_files(self, localFile, remotePath):
        
        client = paramiko.SSHClient()
        smtp = SMTPMail(
            email=os.getenv('emailSender'),
            password=os.getenv('senderPassword')
        )

        ##Conexão com Servidor SFTP
        try:
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(
                hostname = self.host, 
                port = self.port, 
                username = self.user, 
                password = self.password)
        
            print(f"Sucesso ao conectar-se com o servidor SFTP {self.host}\n")
        
            ##Envio de arquivo | put no SFTP
            try:
                sftp = client.open_sftp()
                sftp.put(localFile, remotePath)
        
                sftp.close()
                
                print(f"Sucesso ao enviar arquivos servidor SFTP {self.host}\n")
                #Email de sucesso de envio de arquivo (Stakeholder)
                smtp.status_email(" - ARQUIVOS ENVIADOS", os.getenv('emailsToClient'), "envio de arquivos p/ SFTP" )
                #Email de sucesso de envio de arquivo (Support)
                smtp.status_email(" - SFTP SENT SUCCESS", os.getenv('emailsToSupport'), "envio de arquivos p/ SFTP")


            #Tratamento Erro: Execução do put no servidor SFTP
            except Exception as e:
                print(f"Erro ao enviar arquivo:\n {e}")

                #Email de ERRO de envio de arquivo (Stakeholder)
                smtp.status_email(" - ERRO AO ENVIAR ARQUIVOS", os.getenv('emailsToClient'), "envio de arquivos p/ SFTP", 1, "O Suporte ja foi notificado e logo entrará em contato!")
                #Email de ERRO de envio de arquivo (Support)
                smtp.status_email(" - SFTP SENT FAIL", os.getenv('emailsToSupport'), "envio de arquivos p/ SFTP", 1, str(e))
        
            client.close()

        ##Tratamento Erro: Conexão com Servidor SFTP
        except Exception as e:
            print(f"\n\nErro ao conectar:\n {e}")

            #Email de ERRO de conexão c/ SFTP (Stakeholder)
            smtp.status_email(" - ERRO DE CONEXÃO AO ENVIAR ARQUIVOS", os.getenv('emailsToClient'), "envio de arquivos p/ SFTP", 1, "O Suporte ja foi notificado e logo entrará em contato!")
            #Email de ERRO de conexão c/ SFTP + error (Support)
            smtp.status_email(" - SFTP CONNECTION FAIL", os.getenv('emailsToSupport'), "conexão c/ servidor SFTP ", 1, str(e))



