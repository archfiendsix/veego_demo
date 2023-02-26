import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class YoutubePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def run_youtube_streaming(self, timeout=180):
       
        self.driver.maximize_window()
        

        self.driver.get('https://www.youtube.com/watch?v=jmD254CgmFo')
        
        time.sleep(2)
        # self.actions.send_keys('k').perform()
        self.logger(f'\nPlaying Youtube video... \n')
 
        time.sleep(timeout)
        # 180

    def run_youtube_download(self,timeout=180):
        
        self.driver.maximize_window()
        
        
        self.driver.get('https://www.youtube.com/watch?v=wxmArAaNtNQ')

        try:
            
            downloadedButton_locator = (By.CSS_SELECTOR,'button[aria-label="Downloaded"]')
            downloadedButton = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    downloadedButton_locator)
            )
            downloadedButton.click()
            dialogDelete_locator = (By.CSS_SELECTOR,".yt-confirm-dialog-renderer")
            dialogDelete = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    dialogDelete_locator)
            )
            dialogDelete.click()
        except NoSuchElementException:
            print("Video not downloaded yet.")
            download_button_locator= (By.CSS_SELECTOR, 'button[aria-label="Download"]')
            download_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    download_button_locator)
            )
            download_button.click()
        
        time.sleep(2)
        
        
        self.logger(f'\nStarting Youtube Download... \n')
      
        time.sleep(timeout)
        # 180
