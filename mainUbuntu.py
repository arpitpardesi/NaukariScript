import os
import time
import logging
from contextlib import nullcontext

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import config

# ------------------- Logging Setup -------------------

logging.basicConfig(
    filename='naukri_resume_uploader.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# ------------------- Function Definitions -------------------

def loginNaukri(config, siteConfig):
    logging.info("Navigating to login page.")
    driver.get(siteConfig.get("url"))
    time.sleep(2)
    logging.info("Entering credentials.")

    try:
        username = driver.find_element(By.ID, siteConfig.get('userID'))
        if username:
            username.send_keys(config.username)
            logging.info("Entered username.")

        password = driver.find_element(By.ID, siteConfig.get("passID"))
        if password:
            password.send_keys(config.password)
            password.send_keys(Keys.RETURN)
            logging.info("Password entered and login submitted.")
            time.sleep(5)
    except Exception as e:
        logging.error(f"Login failed: {e}")


def navigateProfile(profileUrl):
    try:
        driver.get(profileUrl)
        logging.info(f"Navigated to profile URL: {profileUrl}")
        time.sleep(2)
    except Exception as e:
        logging.error(f"Error navigating to profile: {e}")


def uploadCV(siteConfig):
    try:
        uploadCV = driver.find_element(By.ID, siteConfig.get('upload'))
        if uploadCV:
            logging.info("Uploading resume.")
            uploadCV.send_keys(siteConfig.get("cv"))
            logging.info(f"Resume uploaded from {siteConfig.get('cv')}")
            time.sleep(5)
    except Exception as e:
        logging.error(f"Failed to upload resume: {e}")


def editProfile():
    logging.info("Editing profile headline.")
    try:
        edit_button = driver.find_element(By.XPATH,
                                          '//span[text()="Resume headline"]/following-sibling::span')
        edit_button.click()
        time.sleep(3)

        save = driver.find_element(By.XPATH, '//button[text()="Save"]')
        save.click()
        logging.info("Profile headline updated successfully.")
        time.sleep(3)
    except Exception as e:
        logging.error(f"Error while editing profile: {e}")


def naukri():
    siteConfig = {
        "url": "https://www.naukri.com/nlogin/login",
        "cv": "/Users/arpitpardesi/Naukri.com Resume/India/resume_arpit.pdf",
        "profileUrl": "https://www.naukri.com/mnjuser/profile",
        "userID": "usernameField",
        "passID": "passwordField",
        "upload": "attachCV",
        "submitId": ""
    }

    loginNaukri(config=config, siteConfig=siteConfig)
    navigateProfile(siteConfig.get("profileUrl"))
    uploadCV(siteConfig=siteConfig)
    editProfile()


def naukriGulf():
    siteConfig = {
        "url": "https://www.naukrigulf.com/jobseeker/login",
        "cv": "/Users/arpitpardesi/Naukri.com Resume/Abroad/resume_arpit.pdf",
        "profileUrl": "https://www.naukrigulf.com/mnj/userProfile/myCV",
        "userID": "loginPageLoginEmail",
        "passID": "loginPassword",
        "submitId": "loginPageLoginSubmit",
        "upload": "resumeSection"
    }

    loginNaukri(config=config, siteConfig=siteConfig)
    navigateProfile(siteConfig.get("profileUrl"))
    uploadCV(siteConfig=siteConfig)

    # ------------------- Script Entry Point -------------------

user = config.username
pwd = config.password
options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
logging.info("Chrome WebDriver initialized successfully.")

logging.info("Script initiated for Naukri.com")
naukri()

# Uncomment to use for NaukriGulf
# logging.info("Script initiated for NaukriGulf.com")
# naukriGulf()

driver.quit()
logging.info("WebDriver closed. Script execution finished.")
