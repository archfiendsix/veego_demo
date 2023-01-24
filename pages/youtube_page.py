import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class YoutubePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def run_youtube(self):
        self.logger(f'\nStarting Youtube test... \n')
        self.driver.get('https://www.youtube.com/watch?v=jmD254CgmFo')
        time.sleep(2)
        self.actions.send_keys('k').perform()
        time.sleep(180)
        #180

        