import paramiko 
import os 
from dotenv import load_dotenv

load_dotenv()

client = paramiko.SSHClient()

try:
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname = os.getenv('sftpServer'), 
        port = os.getenv('sftpPort'), 
        username = os.getenv('sftpUser'), 
        password = os.getenv('sftpPass'))

    print("Sucesso!\n")
    client.close()

except Exception as e:
    print(f"Erro ao conectar: {e}")
