import paramiko

class SFTPService: 

    def __init__(self, host, port, user, password):
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
    

##Conexão com Servidor SFTP
#try:
#    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#    client.connect(
#        hostname = os.getenv('sftpServer'), 
#        port = os.getenv('sftpPort'), 
#        username = os.getenv('sftpUser'), 
#        password = os.getenv('sftpPass'))
#
#    print("Sucesso!\n")
#
#    ##Execução de comando no servidor SFTP
#    try:
#        filePath = os.getenv('filePathLocal')
#        remotePath = os.getenv('filePathRemote')
#
#        sftp = client.open_sftp()
#        sftp.put(filePath, remotePath)
#
#        print("Arquivo enviado com sucesso!")
#        sftp.close()
#
#    #Tratamento Erro: Execução de comando no servidor SFTP
#    except Exception as e:
#        print(f"Erro ao executar comando: {e}")
#
#    client.close()

##Tratamento Erro: Conexão com Servidor SFTP
#except Exception as e:
#    print(f"Erro ao conectar: {e}")


