import paramiko
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

        ##Conexão com Servidor SFTP
        try:
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(
                hostname = self.host, 
                port = self.port, 
                username = self.user, 
                password = self.password)
        
            print(f"Sucesso ao conectar-se com o servidor SFTP!, {hostname}\n")
        
            ##Envio de arquivo | put no SFTP
            try:
                sftp = client.open_sftp()
                sftp.put(localFile, remotePath)
        

                #Email de sucesso de envio de arquivo (Stakeholder)
                
                #Email de sucesso de envio de arquivo (Support)

                sftp.close()
        
            #Tratamento Erro: Execução do put no servidor SFTP
            except Exception as e:
                print(f"Erro ao enviar arquivo:\n {e}")

            #Email de ERRO de envio de arquivo (Stakeholder)
                
            #Email de ERRO de envio de arquivo (Support)
        
            client.close()

        ##Tratamento Erro: Conexão com Servidor SFTP
        except Exception as e:
            print(f"\n\nErro ao conectar:\n {e}")

            #Email de ERRO de conexão c/ SFTP (Stakeholder)
                
            #Email de ERRO de conexão c/ SFTP + error (Support)



