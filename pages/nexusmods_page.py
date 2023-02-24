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
        self.driver.get(self.test_sites["nexusmods_download"])
        
        self.driver.maximize_window()
        # jjk = input('Enter')

        cookies = [
            {'name': 'SSPZ', 'value': '172138'},
            {'name': 'DSP2F_71', 'value': '343983'},
            {'name': 'vs', 'value': '242441=5325914&503171=5082295&219976=5089374&521966=5102021&557984=5282398&497351=5282396'},
            {'name': 'DSP2F_55', 'value': '298424'},
            {'name': 'TAPAD', 'value': "%7B%22id%22%3A%22a0403514-f4c3-452e-8339-d24fb887d075%22%7D"},
            {'name': 'jwt_fingerprint', 'value': 'a67c8658085334bcbb95563244e29cab'},
            {'name': '_hjSessionUser_1264276', 'value': 'eyJpZCI6IjEyODk3NWUwLTA3ZTktNTU5Zi05MjExLWQ2YjI5MDQ5MmQ3ZiIsImNyZWF0ZWQiOjE2NzYyNzcxNTYyMDEsImV4aXN0aW5nIjp0cnVlfQ=='},
            # Add more cookies as needed
        ]

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.save_cookie(self.driver,'/tmp/cookie')
       

        
        time.sleep(60)
        

    def run_nexusmods_download(self):
        self.nexusmods_signin(self.env_nexusmods_email, self.env_nexusmods_password)
        self.logger(f'\nStarting Nexus Mods Download test... \n')
        time.sleep(10)

   