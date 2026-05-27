# SFTP JOBS AUTOMATION
Projeto em Python para automação do envio agendado de arquivos para SFTP com notificações via email SMTP

## Tecnologias
- Python 3.14.5
- Python Dotenv (https://pypi.org/project/python-dotenv/)
- Paramiko (https://docs.paramiko.org/en/stable/)
- Smtplib (https://docs.python.org/3/library/smtplib.html)
- Shutil (https://docs.python.org/3/library/shutil.html)
- Scheduler (https://pypi.org/project/scheduler/)

## Funcionalidades
- Envio de arquivos ao servidor SFTP
- Notificações via email dinâmicas
- Tratamento de exceções
- Organização em camadas de serviço

## Estrutura do Projeto
sftpJobs/
|
|- main.py
|- .env
|
|- services/
|-- emailSmtp.py
|-- filesmanager.py
|-- sftp_service.py

## Fluxo da Aplicação
1. O arquivo `main.py` é executado

2. As variáveis de ambiente são carregadas através do arquivo `.env` utilizando `load_dotenv()`

3. É criada uma instância da classe `SFTPService` com os dados de conexão do servidor SFTP:
   * host
   * porta
   * usuário
   * senha

4. A função `daily_job()` é registrada no scheduler da biblioteca `schedule`.

5. O scheduler permanece em execução contínua através de um loop infinito:
   * verifica tarefas pendentes
   * aguarda 1 segundo entre verificações

6. No horário configurado (`18:32`), o scheduler executa a função `daily_job()`

7. A função `daily_job()` chama o método: client.transport_files(localFile, remotePath)

8. Dentro do método `transport_files()`:
   * é criado um cliente SSH (`paramiko.SSHClient`)
   * é criada uma instância da classe `SMTPMail`

9. A aplicação tenta realizar conexão com o servidor SFTP utilizando:
   * hostname
   * porta
   * usuário
   * senha

10. Em caso de sucesso na conexão:
    * é aberta uma sessão SFTP
    * o arquivo local é enviado ao servidor remoto utilizando `sftp.put()`

11. Após envio concluído:
    * a sessão SFTP é encerrada
    * é enviado e-mail de sucesso para stakeholders
    * é enviado e-mail de sucesso para suporte técnico

12. Após envio bem sucedido:
    * o arquivo local é movido para a pasta de arquivos antigos utilizando: movefileold()

13. Caso ocorra erro durante o upload:
    * o erro é capturado via `except`
    * no dia 28 do mês:
      * stakeholders recebem notificação amigável
      * suporte recebe detalhes técnicos do erro
    * nos demais dias:
      * o erro é apenas exibido no console

14. Caso ocorra falha de conexão com o servidor SFTP:
    * o erro é exibido no console
    * stakeholders recebem alerta de indisponibilidade
    * suporte recebe detalhes técnicos da exceção

15. A classe `SMTPMail` é responsável por:
    * criar mensagens de e-mail
    * autenticar no SMTP Gmail
    * enviar notificações de sucesso e falha

16. A função `get_formated_date()` é utilizada para incluir a data atual formatada nos assuntos e conteúdos dos e-mails.

## Instalação
Para executar o projeto em questão, são necessárias as instalações das dependências citadas, para instala-las use os comandos abaixo:
- pip install paramiko 
- pip install python-dotenv 
- pip install schedule 


## Como executar
- No diretório do projeto basta executar "python main.py" no terminal