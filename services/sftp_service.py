import paramiko

class SFTPService: 

    def __init__(self, host, port, user, password):
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
    

    def transportFiles(self, localFile, remotePath):
        
        client = paramiko.SSHClient()

        ##Conexão com Servidor SFTP
        try:
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(
                hostname = self.host, 
                port = self.port, 
                username = self.user, 
                password = self.password)
        
            print("Sucesso!\n")
        
            ##Envio de arquivo | put no SFTP
            try:
                sftp = client.open_sftp()
                sftp.put(localFile, remotePath)
        
                print("Arquivo enviado com sucesso!")
                sftp.close()
        
            #Tratamento Erro: Execução do put no servidor SFTP
            except Exception as e:
                print(f"Erro ao enviar arquivo:\n {e}")
        
            client.close()

        ##Tratamento Erro: Conexão com Servidor SFTP
        except Exception as e:
            print(f"\n\nErro ao conectar:\n {e}")



