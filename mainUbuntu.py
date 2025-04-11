import os
import time
import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to ChromeDriver on Raspberry Pi
CHROME_DRIVER_PATH = "/usr/bin/chromedriver"

# Configure Chrome options for Raspberry Pi
options = Options()
# options.add_argument("--headless")  # Run in headless mode (no GUI)
options.add_argument("--disable-gpu")  # Disable GPU (fixes errors in headless mode)
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Avoid shared memory issues

# Initialize WebDriver
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)


def login_naukri(config, site_config):
    driver.get(site_config.get("url"))
    time.sleep(7)
    print("Entering credentials")
    try:
        username = driver.find_element(By.ID, site_config.get('userID'))
        if username:
            username.send_keys(config.username)

        password = driver.find_element(By.ID, site_config.get("passID"))
        if password:
            password.send_keys(config.password)
            password.send_keys(Keys.RETURN)
            print("Logged in successfully")
            time.sleep(5)
    except Exception as e:
        print(f"Login failed: {e}")


def navigate_profile(profile_url):
    driver.get(profile_url)
    print("Navigated to the profile")
    time.sleep(5)


def upload_cv(site_config):
    try:
        upload_cv = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, site_config.get('upload')))
        )
        if upload_cv:
            print("Uploading Resume")
            upload_cv.send_keys(site_config.get("cv"))
            print(f"Resume uploaded successfully from {site_config.get('cv')}!")
            time.sleep(5)
    except Exception as e:
        print(f"Unable to upload resume: {e}")


def edit_profile():
    try:
        print("Editing profile")
        edit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Resume headline"]/following-sibling::span'))
        )
        edit_button.click()
        time.sleep(5)
        save = driver.find_element(By.XPATH, '//button[text()="Save"]')
        save.click()
        print("Profile headline updated")
        time.sleep(5)
    except Exception as e:
        print(f"Error editing profile: {e}")


def naukri():
    site_config = {
        "url": "https://www.naukri.com/nlogin/login",
        "cv": "/home/aaa-pi/Documents/Naukri.com Resume/India/resume_arpit.pdf",  # Adjusted path for Raspberry Pi
        "profileUrl": "https://www.naukri.com/mnjuser/profile",
        "userID": "usernameField",
        "passID": "passwordField",
        "upload": "attachCV",
        "submitId": ""
    }

    login_naukri(config, site_config)
    navigate_profile(profile_url=site_config.get("profileUrl"))
    upload_cv(site_config=site_config)
    edit_profile()


print("Script initiated for Naukri.com")
naukri()

driver.quit()