import os 
from dotenv import load_dotenv
#função pra leitura do arquivo .env
load_dotenv()
from services.sftp_service import SFTPService

#Instanciada classe do SFTP Services
client = SFTPService( 
    host=os.getenv('sftpServer'),
    port=os.getenv('sftpPort'),
    user=os.getenv('sftpUser'),
    password=os.getenv('sftpPass')
)

#Instanciada classe do Email SMTP
client.transport_files(
    os.getenv('filePathLocal'), 
    os.getenv('filePathRemote')
)