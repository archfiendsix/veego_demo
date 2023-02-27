import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class TiktokPage(BasePage):
    def __init__(self, driver, test_sites):     
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def twitter_signin(self, twitter_email, twitter_password):
        self.driver.get(self.test_sites["tiktok_social"])
        # wait = WebDriverWait(self.driver, self.timeout).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, '.header__loginMenu button[title="Sign in"]'))
        # )
        # signin_btn = self.driver.find_element(By.CSS_SELECTOR, '.header__loginMenu button[title="Sign in"]')
        # signin_btn.click()

        # time.sleep(3)
        # wait = WebDriverWait(self.driver, self.timeout).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, '.modal.g-z-index-modal-background'))
        # )
        # signin_email_textbox = self.driver.find_element(By.ID, 'sign_in_up_email')
        # signin_email_textbox.send_keys(soundcloud_email)

    def run_tiktok(self,timeout=180):
        
        self.driver.get(self.test_sites["tiktok_social"])
        
        # self.load_cookies()
        # self.twitter_signin(self.env_twitter_email, self.env_twitter_password)
        self.logger(f'\nRunning Tiktok Social... \n')
        time.sleep(timeout)
     

   