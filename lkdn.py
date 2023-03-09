import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Constants
MAX_PAGE_NUMBER = 10
SEARCH_QUERY = "techrecruiter"

# Load environment variables
load_dotenv()
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")

# Set up Selenium
chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome('./chromedriver.exe', options=chrome_options)

def login():
    """
    Logs into LinkedIn with the given credentials.
    """
    driver.get("https://www.linkedin.com/login")
    time.sleep(5)
    driver.find_element(By.ID, "username").send_keys(LOGIN)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, ".btn__primary--large").click()
    time.sleep(5)

def connect():
    """
    Sends connection requests to recruiters matching the given search query.
    """
    current_page_number = 1

    while current_page_number <= MAX_PAGE_NUMBER:
        driver.get(f"https://www.linkedin.com/search/results/people/?keywords={SEARCH_QUERY}&origin=CLUSTER_EXPANSION&page={current_page_number}&sid=!ob")
        time.sleep(5)
        connect_buttons = driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Invite')][span[text()='Connect']]")
        for connect_button in connect_buttons:
            connect_button.click()
            try:
                driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Send now')]").click()
            except:
                pass
            time.sleep(5)
        
        current_page_number += 1

if __name__ == "__main__":
    login()
    connect()