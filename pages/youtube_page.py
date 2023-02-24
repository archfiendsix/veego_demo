import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class YoutubePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def run_youtube_streaming(self):
       
        self.driver.maximize_window()
        

        self.driver.get('https://www.youtube.com/watch?v=jmD254CgmFo')
        
        time.sleep(2)
        self.actions.send_keys('k').perform()
        self.logger(f'\nPlaying Youtube video... \n')
 
        time.sleep(180)
        # 180

    def run_youtube_download(self):
        
        self.driver.maximize_window()
        
        
        self.driver.get('https://www.youtube.com/watch?v=wxmArAaNtNQ')
        
        time.sleep(2)
        download_button_locator= (By.CSS_SELECTOR, 'button[aria-label="Download"]')
        download_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                download_button_locator)
        )
        download_button.click()
        
        self.logger.WARNING(f'\nStarting Youtube Download... \n')
      
        time.sleep(180)
        # 180
