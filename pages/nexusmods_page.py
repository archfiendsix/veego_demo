import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class NexusModsPage(BasePage):
    def __init__(self, driver, test_sites):     
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10
        self.nav_login_button_locator = By.CLASS_NAME,"replaced-login-link"

    def nexusmods_signin(self, nexumods_email, nexusmods_password):
        
        
        self.driver.maximize_window()
        # jjk = input('Enter')

       
       

        
        time.sleep(60)
        

    def run_nexusmods_download(self, timeout=180):
        # self.nexusmods_signin(self.env_nexusmods_email, self.env_nexusmods_password)

        self.driver.get(self.test_sites["nexusmods_download"])
        
        self.driver.maximize_window()

        download_button_locator = (By.CSS_SELECTOR, '#slowDownloadButton')
        download_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(download_button_locator)
        )
        download_button.click()

        self.logger(f'\nStarting Nexus Mods Download test... \n')
        time.sleep(timeout)

   