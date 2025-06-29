import smtplib
from email.message import EmailMessage

class Email:
    def __init__(self, email_from, password, email_to):
        self.email_from = email_from
        self.password = password
        self.email_to = email_to

    def send_email(self, package_status):
        msg = EmailMessage()
        msg['Subject'] = 'Atualização da sua entrega!'
        msg['From'] = self.email_from
        msg['To'] = self.email_to
        msg.set_content(f'''
  Olá! Segue a atualização da sua encomenda do Aliexpress.

{package_status}

Obrigado pela colaboração!
    ''')

        # Envia usando SMTP do Gmail
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email_from, self.password)
                smtp.send_message(msg)

        except Exception as e:
            print(f'Erro ao enviar e-mail: {e}')
