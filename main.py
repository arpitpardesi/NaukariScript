from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import json
import requests
import os
from datetime import datetime, timedelta
import config
from config import username

def login():
    pass

user = config.username
pwd = config.password
url = "https://www.naukri.com/nlogin/login"

options = Options()
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get(url)

login = driver.find_element(By.ID, 'login_Layer')
if login:
    login.click()
time.sleep(3)

username = driver.find_element(By.ID, 'usernameField')
if username:
    username.clear()
    username.send_keys(user)

password = driver.find_element(By.ID, 'passwordField')
if password:
    password.clear()
    password.send_keys(pwd)
    password.send_keys(Keys.RETURN)
time.sleep(3)

# submit = driver.find_element(By.ID, 'g-recaptcha')
# # submit = driver.find_element(By.ID, 'btn-login')
# if submit:
#     submit.click()

# driver.quit()
