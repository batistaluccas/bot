
from selenium import webdriver
import time 

navegador = webdriver.Chrome()
navegador.get('https://login.site.com/')
navegador.maximize_window()

input_login = navegador.find_element('class name', 'cwsuid-input-field')
input_login.send_keys('usuario_usr')

login_button = navegador.find_element('class name', 'Submitbtn')
time.sleep(1) 
login_button.submit()

input_password = navegador.find_element('class name', 'cwspwd-input-field')
input_password.send_keys('password_pwd')

password_button = navegador.find_element('class name', 'Submitbtn')
time.sleep(1)
password_button.submit()

time.sleep(15)  
navegador.quit()