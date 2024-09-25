from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#################----------Amazon-------------##################
# #Keep Chrome browser open after program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")


# driver.close()

#################-----------python.org-------####################3

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.python.org/")
# time = []
# name = []

# for num in range(1, 6):
#     event_date = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{num}]/time')
#     time.append(event_date.text)
# print(time)

# for num in range(1, 6):
#     event_name = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{num}]/a')
#     name.append(event_name.text)
# print(name)

# output2 = {}
# for i in range(len(name)):
#     output2[i] = {
#         "time": time[i],
#         "name": name[i],
#     }
# print(output2)

# driver.quit()


##############----------wiwkipedia------######################

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome browser
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_number = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article_number.click()

# Sending keyboard input to Selenium
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

# driver.quit()