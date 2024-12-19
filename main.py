from selenium import webdriver
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

userName = config.username
password = config.password

options = Options()
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get('http://www.naukri.com')
login = driver.find_element(By.ID, 'login_Layer')
if login:

    login.click()
time.sleep(3)
# driver.quit()
