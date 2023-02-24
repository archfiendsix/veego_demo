import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class SoundcloudPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def soundcloud_signin(self, soundcloud_email, soundcloud_password):

        wait = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.header__loginMenu button[title="Sign in"]'))
        )
        signin_btn = self.driver.find_element(
            By.CSS_SELECTOR, '.header__loginMenu button[title="Sign in"]')
        signin_btn.click()

        time.sleep(3)
        wait = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.modal.g-z-index-modal-background'))
        )
        signin_email_textbox = self.driver.find_element(
            By.ID, 'sign_in_up_email')
        signin_email_textbox.send_keys(soundcloud_email)

    def run_soundcloud_music(self):
        # self.dump_cookies()
        
        self.driver.get(self.test_sites["soundcloud_music"])
        # self.driver.get("https://www.facebook.com")
        time.sleep(30)
        # Set the maximum amount of time to wait for the element to be present
        self.driver.maximize_window()
        timeout = 10
        # # Create a wait object with the specified timeout and expected condition
        # wait = WebDriverWait(self.driver, timeout).until(
        #     EC.presence_of_element_located(
        #         (By.ID, "onetrust-accept-btn-handler"))
        # )
        # save_cookies_accept_btn = self.driver.find_element(
        #     By.ID, "onetrust-accept-btn-handler")
        play_btn_locator = (By.CSS_SELECTOR, ".sc-button-play.playButton.sc-button.m-stretch")
        play_btn = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(
                play_btn_locator)
        )
        play_btn.click()

       
        
        self.logger(f'\nStarting Soundcloud play test... \n')

        # self.dump_cookies()
        # self.load_cookies()
        time.sleep(20)
       
    def run_soundcloud_upload(self):
        self.logger('Starting Soundcloud upload test...')
        
        # Load the Soundcloud upload page
        self.driver.maximize_window()
        self.driver.get(self.test_sites["soundcloud_upload"])
        
        time.sleep(3)

        # Handle cookies dialog if present
        # save_cookies_accept_btn = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        # save_cookies_accept_btn.click()

        # Sign in to Soundcloud if necessary
        # self.soundcloud_signin(self.env_soundcloud_email, self.env_soundcloud_password)

        # Select the file to upload
        file_input_locator = (By.CSS_SELECTOR, ".chooseFiles .chooseFiles__input")
        file_upload_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(file_input_locator)
        )
        file_path = os.path.abspath("fixtures/music.mp3")
        file_upload_input.send_keys(file_path)

        save_button_locator = (By.CSS_SELECTOR, 'button[title="Save"]')
        save_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(save_button_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", save_button)
        save_button.click()
        self.dump_cookies()
        self.load_cookies()
        # Wait for the upload to complete
        time.sleep(20)
        
        # 180
