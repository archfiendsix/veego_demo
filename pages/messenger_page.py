import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class MessengerPage(BasePage):
    def __init__(self, driver):     
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def run_messenger_conference(self, timeout=180):
        self.logger(f'\nStarting Messenger Conferencing test... \n')
        self.driver.maximize_window()
        self.driver.get('https://www.messenger.com/')
        time.sleep(10)
        continue_as_locator = (By.CSS_SELECTOR,'button["type="submit"]')
        continue_as_btn = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                continue_as_locator)
        )
        # continue_as_btn = self.driver.find_element(By.XPATH,'//button[contains(text(), "Continue")]')
        continue_as_btn.click()

        
        time.sleep(timeout)
        
