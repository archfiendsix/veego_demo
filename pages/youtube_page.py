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
        

    def run_youtube(self):
        print('\nStarting Youtube test... \n')
        # time.sleep(2)
        self.driver.get('https://www.youtube.com/watch?v=jmD254CgmFo')
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys('k')
        actions.perform()
        time.sleep(180)
        #180

        