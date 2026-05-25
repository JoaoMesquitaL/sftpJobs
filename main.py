import paramiko 
import os 
from dotenv import load_dotenv

load_dotenv()

client = paramiko.SSHClient()

##Conexão com Servidor SFTP
try:
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname = os.getenv('sftpServer'), 
        port = os.getenv('sftpPort'), 
        username = os.getenv('sftpUser'), 
        password = os.getenv('sftpPass'))

    print("Sucesso!\n")

    ##Execução de comando no servidor SFTP
    try:

        stdin, stdout, stderr = client.exec_command("cd sftpServer && dir")

        resultado = stdout.read().decode('latin-1')
        erro = stderr.read().decode('latin-1')

        ##Essa estrutura permite a exibição do objeto de erro do exec_command
        if erro:
            print("Erro:")
            print(erro)
        else:
            print("Resultado:")
            print(resultado)

    #Tratamento Erro: Execução de comando no servidor SFTP
    except Exception as e:
        print(f"Erro ao executar comando: {e}")
    
    client.close()

##Tratamento Erro: Conexão com Servidor SFTP
except Exception as e:
    print(f"Erro ao conectar: {e}")
