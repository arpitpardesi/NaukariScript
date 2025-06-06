import os
from contextlib import nullcontext

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

import time
import config


def loginNaukri(config, siteConfig):
    driver.get(siteConfig.get("url"))
    time.sleep(2)
    print("Entering credentials")
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
            print("Logged in successfully")
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

    print("Navigated to the profile")
    time.sleep(2)


def uploadCV(siteConfig):
    uploadCV = driver.find_element(By.ID, siteConfig.get('upload'))
    # uploadCV = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.ID, siteConfig.get('upload')))
    # )

    # uploadCV = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, '[id="attachCV"]'))
    # )
    # uploadCV = driver.find_element(By.ID, 'result')
    if uploadCV:
        try:
            print("Uploading Resume")
            uploadCV.send_keys(siteConfig.get("cv"))

            print(f"Resume uploaded successfully from {siteConfig.get('cv')}!")


            time.sleep(5)
        except:
            print("Unable to find the Resume upload input field!")


def editProfile():
    print("Editing profile")
    edit_button = driver.find_element(By.XPATH,
                                      '//span[text()="Resume headline"]/following-sibling::span')  # Adjust XPATH if needed
    edit_button.click()
    time.sleep(3)
    save = driver.find_element(By.XPATH,
                               '//button[text()="Save"]')
    save.click()
    print("Profile headline updated")
    time.sleep(3)



def naukri():
    siteConfig = {"url": "https://www.naukri.com/nlogin/login",
                  "cv": "/Users/arpitpardesi/Naukri.com Resume/India/resume_arpit v2.pdf",
                  "profileUrl": "https://www.naukri.com/mnjuser/profile",
                  "userID": "usernameField",
                  "passID": "passwordField",
                  "upload": "attachCV",
                  "submitId": ""}

    loginNaukri(config=config, siteConfig=siteConfig)
    navigateProfile(profileUrl=siteConfig.get("profileUrl"))
    uploadCV(siteConfig=siteConfig)
    editProfile()
    # driver.quit()


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

    # driver.quit()


user = config.username
pwd = config.password
options = Options()
# options.add_argument("--headless")  # Runs Chrome in headless mode
# options.add_argument("--disable-gpu")  # Disable GPU acceleration for headless mode
# options.add_argument("--no-sandbox")  # Disable sandbox for compatibility
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

# Set up the WebDriver for Chromium (for Raspberry Pi)

# options.add_argument("--headless")  # Runs Chrome in headless mode
# options.add_argument("--disable-gpu")  # Disable GPU acceleration for headless mode
# options.add_argument("--no-sandbox")  # Disable sandbox for compatibility
# chrome_driver_path = '/usr/bin/chromedriver'  # Ensure chromedriver is in the correct path
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service, options=options)

print("Script initiated for Naukri.com")
naukri()

# print("Script initiated for NaukriGulf.com")
# naukriGulf()

driver.quit()
