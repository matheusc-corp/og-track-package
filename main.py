"""
Tu precisa abrir o site do governo, e rastrear minha entrega,
enviar um email para mim para eu saber o estado da minha entrega

Rastreio: CNBR00077223717
O rastreio vai ser no site da AliExpress Selection Standard

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com.br')
time.sleep(2)

