from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getnev("EMAIL")
PASSWORD = os.getnev("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome browser
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3974285202&distance=25&f_AL=true&geoId=105365761&keywords=Python%20Developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

time.sleep(10)
try:
    ##---------------TOP-RIGHT BUTTON-------------##
    sign_up_button = driver.find_element(By.XPATH, value="/html/body/div[2]/a[1]")
    sign_up_button.click()
    
    time.sleep(10)
    email = driver.find_element(By.ID, value="username")
    email.send_keys("nwaohasuccess2306@gmail.com")
    
    password = driver.find_element(By.ID, value="password")
    password.send_keys("$Weaderreader232006$")
    password.send_keys(Keys.ENTER)

    
except:
    try:
        ##-----------------COVER-SCREEN POP-UP-----------------##
        # sign_up_button = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[1]/button')
        # sign_up_button.click()
        
        exit_button = driver.find_element(By.CSS_SELECTOR, value='#base-contextual-sign-in-modal > div > section > button > icon > svg')
        exit_button.click()
        
        sign_up_button = driver.find_element(By.XPATH, value="/html/body/div[2]/a[1]")
        sign_up_button.click()
        
        email = driver.find_element(By.ID, value="username")
        email.send_keys("nwaohasuccess2306@gmail.com")
        
        password = driver.find_element(By.ID, value="password")
        password.send_keys("$Weaderreader232006$")
        password.send_keys(Keys.ENTER)
        
    except:
        ##------------------LITTLE POP-UP---------------------##
        sign_up_button = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
        sign_up_button.click()
        
        time.sleep(10)
        email = driver.find_element(By.ID, value="username")
        email.send_keys("nwaohasuccess2306@gmail.com")
        
        password = driver.find_element(By.ID, value="password")
        password.send_keys("$Weaderreader232006$")
        password.send_keys(Keys.ENTER)

# locate the apply button
save_button = driver.find_element(By.CSS_SELECTOR, value="#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.jobs-search__job-details--container > div > div:nth-child(1) > div > div:nth-child(1) > div > div.relative.job-details-jobs-unified-top-card__container--two-pane > div > div.mt5 > div > button")
save_button.click()

# follow_button = driver.find_element(By.CSS_SELECTOR, value="#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.jobs-search__job-details--container > div > div:nth-child(1) > div > section > section > div.jobs-company__box > div.display-flex.align-items-center.mt5 > button")
# follow_button.click()

follow_button = driver.find_element(By.CSS_SELECTOR, value="#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.jobs-search__job-details--container > div > div:nth-child(1) > div > section > section > div.jobs-company__box > div.display-flex.align-items-center.mt5 > button > svg")
follow_button.click()