from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import config

user = config.username
pwd = config.password
options = Options()
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://www.naukrigulf.com/jobseeker/login")
time.sleep(2)

username = driver.find_element(By.ID, "loginPageLoginEmail")
if username:
    # username.clear()
    username.send_keys(config.username)

password = driver.find_element(By.ID, "loginPassword")
if password:
    # password.clear()
    password.send_keys(config.password)
    time.sleep(3)
    # driver.find_element(By.ID,'loginPageLoginSubmit').send_keys(Keys.RETURN)
    password.send_keys(Keys.RETURN)
    time.sleep(5)

driver.quit()
