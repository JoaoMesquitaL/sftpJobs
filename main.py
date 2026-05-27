import os 
from dotenv import load_dotenv
load_dotenv()
from services.sftp_service import SFTPService
import schedule 
import time

#Instanciada classe do SFTP Services
client = SFTPService( 
    host=os.getenv('sftpServer'),
    port=os.getenv('sftpPort'),
    user=os.getenv('sftpUser'),
    password=os.getenv('sftpPass')
)

#definido job a ser chamado pelo scheduler
def daily_job():
    client.transport_files(
        os.getenv('filePathLocal'), 
        os.getenv('filePathRemote')
    )

#Schedulada chamada diária da função de transporte de arquivos
schedule.every().day.at("18:32").do(daily_job)

while True:
    schedule.run_pending()
    time.sleep(1)
