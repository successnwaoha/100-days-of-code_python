from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome browser
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")
money = driver.find_element(By.ID, value="money")

items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 20
five_min = time.time() + 60*10


keep_tapping = True
while keep_tapping:
    cookie.click()
    
    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []
        
        for price in all_prices:
            element_text = price.text
            print(element_text)
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]
        
        money = driver.find_element(By.ID, value="money").text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)
        
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
                
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        
        driver.find_element(By.ID, value=to_purchase_id).click()
        
        timeout = time.time() + 20
    
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, value="cps").text
        print(cookie_per_s)
        break
                
    