import os
from contextlib import nullcontext

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import config


def loginNaukri(config, siteConfig):
    driver.get(siteConfig.get("url"))
    time.sleep(2)

    try:
        username = driver.find_element(By.ID, siteConfig.get('userID'))
        if username:
            # username.clear()
            username.send_keys(config.username)

        password = driver.find_element(By.ID, siteConfig.get("passID"))
        if password:
            # password.clear()
            password.send_keys(config.password)

            password.send_keys(Keys.RETURN)
            time.sleep(5)
            # if siteConfig['submitId']:
            #     submit = driver.find_element(By.ID, siteConfig.get("submitId"))
            #     if submit:
            #         # password.clear()
            #         submit.send_keys(Keys.RETURN)
            # else:
            #     password.send_keys(Keys.RETURN)
    except:
        pass


def navigateProfile(profileUrl):
    driver.get(profileUrl)
    time.sleep(2)


def uploadCV(siteConfig):
    uploadCV = driver.find_element(By.ID, siteConfig.get('upload'))
    # uploadCV = driver.find_element(By.ID, 'result')
    if uploadCV:
        try:
            uploadCV.send_keys(siteConfig.get("cv"))
            time.sleep(5)
            print(f"Resume uploaded successfully from {siteConfig.get('cv')}!")
        except:
            print("Unable to find the Resume upload input field!")


def naukri():
    siteConfig = {"url": "https://www.naukri.com/nlogin/login",
                  "cv": "/Users/arpitpardesi/Naukri.com Resume/India/resume_arpit.pdf",
                  "profileUrl": "https://www.naukri.com/mnjuser/profile",
                  "userID": "usernameField",
                  "passID": "passwordField",
                  "upload": "attachCV",
                  "submitId": ""}

    loginNaukri(config=config, siteConfig=siteConfig)
    navigateProfile(profileUrl=siteConfig.get("profileUrl"))
    uploadCV(siteConfig=siteConfig)

    driver.quit()


def naukriGulf():
    siteConfig = {"url": "https://www.naukrigulf.com/jobseeker/login",
                  "cv": "/Users/arpitpardesi/Naukri.com Resume/Abroad/resume_arpit.pdf",
                  "profileUrl": "https://www.naukrigulf.com/mnj/userProfile/myCV",
                  "userID": "loginPageLoginEmail",
                  "passID": "loginPassword",
                  "submitId": "loginPageLoginSubmit",
                  "upload": "resumeSection"}

    loginNaukri(config=config, siteConfig=siteConfig)
    navigateProfile(profileUrl=siteConfig.get("profileUrl"))
    uploadCV(siteConfig=siteConfig)

    driver.quit()


user = config.username
pwd = config.password
options = Options()
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

naukri()
# naukriGulf()

driver.quit()
