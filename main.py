import os 
from dotenv import load_dotenv
from services.sftp_service import SFTPService

#função pra leitura do arquivo .env
load_dotenv()

#Instanciada classe do SFTP Services
client = SFTPService( 
    host=os.getenv('sftpServer'),
    port=os.getenv('sftpPort'),
    user=os.getenv('sftpUser'),
    password=os.getenv('sftpPass')
)

#Chamado método para envio com parametros
client.transport_files(os.getenv('filePathLocal'), os.getenv('filePathRemote'))