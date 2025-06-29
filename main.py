"""
Tu precisa abrir o site do governo, e rastrear minha entrega,
enviar um email para mim para eu saber o estado da minha entrega

Rastreio: CNBR00077223717
O rastreio vai ser no site da AliExpress Selection Standard

"""

from Track import Track
from Email import Email
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()

    email_from = ''
    email_to = ''
    password = ''

    try:
        track = Track(driver)
        package_status = track.track_package('CNBR00077223717')

        email = Email(email_from, password, email_to)
        email.send_email(package_status.text)

    except Exception as e:
        print(f'Error: {e}')
