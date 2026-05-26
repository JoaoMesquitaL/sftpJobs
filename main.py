import os 
from dotenv import load_dotenv

from services.sftp_service import SFTPService

load_dotenv()

#Instanciada classe do SFTP Services
client = SFTPService( 
    host=os.getenv('sftpServer'),
    port=os.getenv('sftpPort'),
    user=os.getenv('sftpUser'),
    password=os.getenv('sftpPass')
)

