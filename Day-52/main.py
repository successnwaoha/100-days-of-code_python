##### To be completed when broadband is available #####

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

SIMILAR_ACCOUNT = "openai"
USERNAME = "simply_todoroki"
PASSWORD = "$officialaccount232006$"


class InstaFollower:
    
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
    
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(20)
        
        #Check for cookies
        username = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
        password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))
        
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        
        time.sleep(4)
        password.send_keys(Keys.ENTER)
        
        time.sleep(20)
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(20)
        notifications_prompt = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, '_a9-- _ap36 _a9_1') and contains(text(), 'Not Now')]")))
        try:
            if notifications_prompt:
                notifications_prompt.click()
        except Exception as e:
            print(f"Error encountered: {e}")
            print("Element not found within the timeout. Retrying...")
            notifications_prompt.click()
            
            
    def find_followers(self):
        time.sleep(10)
        #Show followers from the selected account
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        
        time.sleep(20)
        modal_xpath = "//div[contains(@style, 'overflow: hidden auto')]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        print(modal)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop +=50", modal)
            time.sleep(6)
        
        
        # search_button = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_Na"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/span/div/a/div')
        # search_input = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_t2"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/nav/div/header/div/h1/div/div/div/div/div/div/label/input')
        # account = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_t2"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/ul/li[1]/a/div')
        # open_followers = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_t2"]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[4]/ul/li[2]/div/a/span')
        
        
        # search_button.click()
        # search_input.send_keys(SIMILAR_ACCOUNT)
        # account.click()
        # open_followers.click()
    
    def follow(self):
        pass




bot = InstaFollower()
bot.login()
time.sleep(10)
bot.find_followers()
time.sleep(10)
bot.follow()


#Username
#//*[@id="loginForm"]/div/div[1]/div/label/input

#Password
#//*[@id="loginForm"]/div/div[2]/div/label/input

#Log in
#//*[@id="loginForm"]/div/div[3]/button

#Not now
#//*[@id="mount_0_0_q2"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div

#Cancel
#/html/body/div[8]/div[1]/div/div/div/div[3]/button[2]

#Not now
#/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[5]/div[2]/div[1]/div/div/div[6]/div/div

#Search button
#//*[@id="mount_0_0_pU"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/span/div/a/div

#Search input
#//*[@id="mount_0_0_t2"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/nav/div/header/div/h1/div/div/div/div/div/div/label/input

#Open ai
#//*[@id="mount_0_0_t2"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/ul/li[1]/a/div
#//*[@id="mount_0_0_c/"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/nav/div/header/div/h1/div/div/div/div/div/div[3]/div/div[2]/div/div[1]/a/div

#Followers
#//*[@id="mount_0_0_t2"]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[4]/ul/li[2]/div/a/span

#Scroll
#/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]

#Follow
##mount_0_0_t2 > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y.x8vgawa > section > main > div > div:nth-child(2) > div > div:nth-child(3) > div > div > div > div:nth-child(3) > div > button
##mount_0_0_t2 > div > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y.x8vgawa > section > main > div > div:nth-child(2) > div > div:nth-child(4) > div > div > div > div:nth-child(3) > div > button