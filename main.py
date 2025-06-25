"""
Tu precisa abrir o site do governo, e rastrear minha entrega,
enviar um email para mim para eu saber o estado da minha entrega

Rastreio: CNBR00077223717
O rastreio vai ser no site da AliExpress Selection Standard

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get('https://www.ordertracker.com/couriers/aliexpress')
time.sleep(5)

wait = WebDriverWait(driver, 15)
searchInput = driver.find_element(By.TAG_NAME, 'input')

searchInput.send_keys('CNBR00077223717')
time.sleep(1)
searchInput.submit()

time.sleep(10)
getStatus = driver.find_element(By.CLASS_NAME, 'status-content')

print(getStatus.text)




