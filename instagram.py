from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
load_dotenv()
from time import sleep

class Instagram:
    def __init__(self):
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.driver = None
        self.username = ""
        self.url = "https://www.instagram.com"
    def set_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver: webdriver.Chrome = webdriver.Chrome(options=chrome_options)
        self.driver.get(url=self.url)
        sleep(1)
    def login(self):
        email_field = self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        email_field.send_keys(self.email)
        password_field = self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password_field.send_keys(self.password)
        login_button = self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div[1]/div[3]/button')
        login_button.click()
        sleep(15)
    def search_account(self,username):
        self.username = username
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()
        sleep(10)
        self.driver.get(url=f'https://www.instagram.com/{username}/')
        sleep(10)

    def follow(self, no_of_accounts):
        username_followers_list = self.driver.find_element(By.XPATH, value=f"//a[@href='/{self.username}/followers/']")
        username_followers_list.click()
        sleep(5)
        while True:
            try:
                # Use find_elements to capture a list of "Follow" buttons
                follow_buttons = self.driver.find_elements(By.XPATH, value="//button[normalize-space(text())='Follow']")
                if not follow_buttons:
                    print("No follow buttons found")
                    break
                for button in follow_buttons:
                    if not no_of_accounts:
                        return True
                    no_of_accounts -= 1
                    button.click()
                    sleep(1)
            except NoSuchElementException:
                print("No more follow buttons")
                break
            else:
                sleep(1)