from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class InstaFollower:

    def __init__(self):
        service = Service(r"C:\Users\dough\OneDrive\Documents\chromedriver\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)

    def login(self, email, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        inputs = self.driver.find_elements(By.CSS_SELECTOR, "input")
        inputs[0].send_keys(email)
        inputs[1].send_keys(password)
        inputs[1].send_keys(Keys.ENTER)
        time.sleep(5)
        buttons = self.driver.find_elements(By.CSS_SELECTOR, "button")
        buttons[1].click()
        time.sleep(5)
        no_notifications = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[3]/button[2]")
        no_notifications.click()
        time.sleep(2)

    def find_followers(self, follow_site):
        search = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(follow_site)
        time.sleep(1)
        insta_click = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[2]/div')
        insta_click.click()
        time.sleep(3)
        follower_click = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div')
        follower_click.click()
        time.sleep(2)
        scrollable = self.driver.find_element(By.CSS_SELECTOR, "li button")
        scrollable.send_keys(Keys.END)
        time.sleep(300)

    def follow(self):
        to_follow = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for followable in to_follow:
            followable.click()
