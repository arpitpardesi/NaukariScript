import os

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from dotenv import load_dotenv
import config

def loginNaukri(url, config):

    options = Options()
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(2)

    username = driver.find_element(By.ID, 'usernameField')
    if username:
        # username.clear()
        username.send_keys(config.username)

    password = driver.find_element(By.ID, 'passwordField')
    if password:
        # password.clear()
        password.send_keys(config.password)
        password.send_keys(Keys.RETURN)
    time.sleep(3)

def navigateProfile():
    driver.get('https://www.naukri.com/mnjuser/profile')
    time.sleep(2)

def uploadCV(cv):
    uploadCV = driver.find_element(By.ID, 'attachCV')
    # uploadCV = driver.find_element(By.ID, 'result')
    if uploadCV:
        try:
            uploadCV.send_keys(cv)
            time.sleep(5)
            print(f"Resume uploaded successfully from {cv}!")
        except:
            print("Unable to find the Resume upload input field!")

user = config.username
pwd = config.password

url = "https://www.naukri.com/nlogin/login"
# cv = "smb://Cosmos._smb._tcp.local/NAS/Documents/MS/Resume/Naukari.com Resume/India/resume_arpit.pdf"
cv = "/Users/arpitpardesi/Naukri.com Resume/India/resume_arpit.pdf"

options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get(url)

# login = driver.find_element(By.ID, 'login_Layer')
# if login:
#     login.click()
# time.sleep(3)

username = driver.find_element(By.ID, 'usernameField')
if username:
    # username.clear()
    username.send_keys(user)

password = driver.find_element(By.ID, 'passwordField')
if password:
    # password.clear()
    password.send_keys(pwd)
    password.send_keys(Keys.RETURN)
time.sleep(3)

driver.get('https://www.naukri.com/mnjuser/profile')
# submit = driver.find_element(By.ID, 'g-recaptcha')
# # submit = driver.find_element(By.ID, 'btn-login')
# if submit:
#     submit.click()
time.sleep(2)
uploadCV = driver.find_element(By.ID, 'attachCV')
# uploadCV = driver.find_element(By.ID, 'result')
if uploadCV:
    try:
        uploadCV.send_keys(cv)
        time.sleep(5)
        print(f"Resume uploaded successfully from {cv}!")
    except:
        print("Unable to find the Resume upload input field!")

driver.quit()
