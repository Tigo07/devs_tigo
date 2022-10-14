def enviando_email(job):

    #print('ENVIANDO EMAIL')
    #print('------------------------------------')
    ###############################################################
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    # para enviar anexos
    from email.mime.base import MIMEBase
    from email import encoders

    # Configuração
    host = 'smtp.office365.com'
    port = 587
    user = 'relatorios@gruposc.com.br'
    password = 'a123456*'

    # Criando objeto
    #print('Criando objeto servidor...')
    server = smtplib.SMTP(host, port)

    # Login com servidor
    #print('Login...')
    server.ehlo()
    server.starttls()
    server.login(user, password)

    # Criando mensagem
    message = ''' 
    Bom dia,

    A tarefa que atualiza o '''+job+''' foi executado com sucesso.

    Sem mais,

    André Ramos
    Depto  IM.
    '''

    ### message_html = '''
    ### <html>
    ###   <head></head>
    ###   <body>
    ###     <p>Olá!<br>
    ###        Como você está?<br>
    ###        Aqui vai um <a href="http://www.python.org">link</a> que talvez você goste.
    ###     </p>
    ###   </body>
    ### </html>
    ### '''

    #print('Criando mensagem...')
    email_msg = MIMEMultipart()
    email_msg['From'] = user

    ### especifique os emails que vão receber
    recipients = 'andre.ramos@gruposc.com.br,tiago.prazeres@gruposc.com.br'
    ###email_msg['To'] = 'andre.ramos@gruposc.com.br'
    email_msg['To'] = recipients
    email_msg['Subject'] = job
    print('Adicionando texto...')
    email_msg.attach(MIMEText(message, 'plain'))     ### qdo for msg simples
    ### email_msg.attach(MIMEText(message_html, 'html'))   ### qdo for msg HTML

    #########################
    #  anexando arquivo
    #########################
    #print('Obtendo arquivo...')
    #filename = str(nomeArquivo) 
    #filepath = '//10.41.14.62/qlik_sc/QlikView_STCRUZ/PRD/12.Arquivos/12/'+str(nomeArquivo)
    #attachment = open(filepath, 'rb')

    #print('Lendo arquivo...')
    #att = MIMEBase('application', 'octet-stream')
    #att.set_payload(attachment.read())
    #encoders.encode_base64(att)
    #att.add_header('Content-Disposition', f'attachment; filename= {filename}')

    #attachment.close()
    #print('Adicionando arquivo ao email...')
    #email_msg.attach(att)

    # Enviando mensagem
    #print('Enviando mensagem...')
    ###server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
    server.sendmail(email_msg['From'], recipients.split(','), email_msg.as_string())

    print('Mensagem enviada!')
    server.quit()
