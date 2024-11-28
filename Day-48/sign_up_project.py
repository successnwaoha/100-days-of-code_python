from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

FIRST_NAME = os.getenv("FIRST_NAME")
LAST_NAME = os.getenv("LAST_NAME")
EMAIL = os.getenv("EMAIL")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome browser
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys(FIRST_NAME)

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys(LAST_NAME)

email = driver.find_element(By.NAME, value="email")
email.send_keys(EMAIL)

sign_up_button = driver.find_element(By.CSS_SELECTOR, value="body > form > button")
sign_up_button.send_keys(Keys.ENTER)