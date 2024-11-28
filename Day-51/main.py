##### To be completed when broadband is available #####

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PROMISED_UP = 10
PROMISED_DOWN = 150
CHROME_DRIVER_PATH = "/Users/PC/Desktop/success/python/100-days-of-code_python/Day-51"
TWITTER_USERNAME = "todoroki2306"
TWITTER_PASSWORD = "U5mmk6$3WRvBWWi"

class InternetSpeedTwitterBot:
    
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0
        
    def get_internet_speed(self):
        # self.driver.get("https://www.speedtest.net/")
        # time.sleep(5)
        
        # #Continue
        # click_continue = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')))
        # click_continue.click()
        # time.sleep(5)
        
        # #Go
        # click_go = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')))
        # click_go.click()
        # time.sleep(200)
        
        # #Download
        # self.down = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')))
        # self.down = self.down.text
        # print(f"This is the download {self.down}")
        
        # #Upload
        # self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        # print(f"This is the upload {self.up}")
        pass
        
    
    def tweet_at_provider(self):
        self.driver.get("https://x.com/")
        #Cancel
        cancel_1 = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div/div[2]/div/div/div/button')))
        cancel_1.click()
        
        #Sign up
        sign_up_button = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a')))
        sign_up_button.click()
        time.sleep(20)
        
        #Username
        enter_username = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        enter_username.send_keys(TWITTER_USERNAME)
        
        #Next
        click_next = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')))
        click_next.click()
        
        #Password
        enter_password = self.driver.find_element(By.NAME, value='password')
        enter_password.send_keys(TWITTER_PASSWORD)
        
        #Login
        login = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        login.click()
        
        #Cancel 2
        cancel_2 = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div[1]/div/div/div/button')
        cancel_2.click()
        
        #Post input
        make_post = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        make_post.send_keys(f"Hey @MTNNG my internet speed is {self.down}down/{self.up}up, is it fair?")
        
        #Post
        post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post.click()
    
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
print(f"Download speed: {bot.down}Mbps")
print(f"Upload speed: {bot.up}Mbps")
bot.tweet_at_provider()

#sign up
# //*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a/div

#input
#//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input

#next
#//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]

#password
#//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input

#log in
#//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button

#cancel 2
#//*[@id="layers"]/div/div[1]/div/div/div/button

#post input
#//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div

#post
#//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button