import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class IcloudPage(BasePage):
    def __init__(self, driver, test_sites):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

    def icloud_signin(self, nexumods_email, nexusmods_password):
        self.driver.get(self.test_sites["icloud_download"])

        self.driver.maximize_window()
        # jjk = input('Enter')

        cookies = [
            {'name': 'SSPZ', 'value': '172138'},
            {'name': 'DSP2F_71', 'value': '343983'},
            {'name': 'vs', 'value': '242441=5325914&503171=5082295&219976=5089374&521966=5102021&557984=5282398&497351=5282396'},
            {'name': 'DSP2F_55', 'value': '298424'},
            {'name': 'TAPAD', 'value': "%7B%22id%22%3A%22a0403514-f4c3-452e-8339-d24fb887d075%22%7D"},
            {'name': 'jwt_fingerprint', 'value': 'a67c8658085334bcbb95563244e29cab'},
            {'name': '_hjSessionUser_1264276',
                'value': 'eyJpZCI6IjEyODk3NWUwLTA3ZTktNTU5Zi05MjExLWQ2YjI5MDQ5MmQ3ZiIsImNyZWF0ZWQiOjE2NzYyNzcxNTYyMDEsImV4aXN0aW5nIjp0cnVlfQ=='},
            # Add more cookies as needed
        ]

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.save_cookie(self.driver, '/tmp/cookie')

        time.sleep(60)

    def icloud_signin(self, nexumods_email, nexusmods_password):
        self.driver.get(self.test_sites["icloud_upload"])

        self.driver.maximize_window()
        # jjk = input('Enter')

        cookies = [
            {'name': 'SSPZ', 'value': '172138'},
            {'name': 'DSP2F_71', 'value': '343983'},
            {'name': 'vs', 'value': '242441=5325914&503171=5082295&219976=5089374&521966=5102021&557984=5282398&497351=5282396'},
            {'name': 'DSP2F_55', 'value': '298424'},
            {'name': 'TAPAD', 'value': "%7B%22id%22%3A%22a0403514-f4c3-452e-8339-d24fb887d075%22%7D"},
            {'name': 'jwt_fingerprint', 'value': 'a67c8658085334bcbb95563244e29cab'},
            {'name': '_hjSessionUser_1264276',
                'value': 'eyJpZCI6IjEyODk3NWUwLTA3ZTktNTU5Zi05MjExLWQ2YjI5MDQ5MmQ3ZiIsImNyZWF0ZWQiOjE2NzYyNzcxNTYyMDEsImV4aXN0aW5nIjp0cnVlfQ=='},
            # Add more cookies as needed
        ]
        
        # self.dump_cookies()
        # self.load_cookies()
        time.sleep(60)

    def delete_file(self):
        self.driver.get(self.test_sites["icloud_upload"])
        
        self.driver.maximize_window()
        time.sleep(15)
        # find the iframe element
        iframe_locator = (By.CSS_SELECTOR, 'iframe[data-name="iclouddrive"]')
        iframe = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                iframe_locator)
        )

        # switch to the iframe
        self.driver.switch_to.frame(iframe)

        browseButton_locator = (
            By.XPATH, "//span[contains(text(), 'Browse')]")
        browseButton = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                browseButton_locator)
        )
        browseButton.click()

        first_file_locator = (
            By.CSS_SELECTOR, 'div[role="listitem"]')
        first_file = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                first_file_locator)
        )
        first_file.click()

        delete_button_locatot = (
            By.CSS_SELECTOR, 'ui-button[title="Delete"]')
        delete_button = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                delete_button_locatot)
        )
        delete_button.click()

        # self.dump_cookies()
        # self.load_cookies()

    def run_icloud_upload(self):
        self.delete_file()
        # self.icloud_signin(self.env_nexusmods_email, self.env_nexusmods_password)

        self.driver.get(self.test_sites["icloud_upload"])
        
        self.driver.maximize_window()
        time.sleep(15)
        # find the iframe element
        iframe_locator = (By.CSS_SELECTOR, 'iframe[data-name="iclouddrive"]')
        iframe = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                iframe_locator)
        )

        # switch to the iframe
        self.driver.switch_to.frame(iframe)

        browseButton_locator = (
            By.XPATH, "//span[contains(text(), 'Browse')]")
        browseButton = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                browseButton_locator)
        )
        browseButton.click()

        input_element_locator = (By.CSS_SELECTOR, '.upload-input-element')
        input_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                input_element_locator)
        )

        input_element.send_keys("fixtures/upload_files/gparted.iso")

        self.logger(f'\nStarting iCloud Upload test... \n')
        # self.dump_cookies()
        # self.load_cookies()
        #

        time.sleep(180)

    def run_icloud_download(self):
        # self.icloud_signin(self.env_nexusmods_email, self.env_nexusmods_password)

        self.driver.get(self.test_sites["icloud_download"])
        
        self.driver.maximize_window()
        # find the iframe element
        iframe_locator = (By.CSS_SELECTOR, 'iframe[data-name="iclouddrive"]')
        iframe = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                iframe_locator)
        )

        # switch to the iframe
        self.driver.switch_to.frame(iframe)
       

        browseButton_locator = (
            By.XPATH, "//span[contains(text(), 'Browse')]")
        browseButton = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                browseButton_locator)
        )

        # browseButton = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Browse')]")
        browseButton.click()

        first_file_locator = (
            By.XPATH, "//span[contains(text(), 'gparted-…-amd64')]")
        first_file = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(
                first_file_locator)
        )
        first_file.click()

        self.logger(f'\nStarting iCloud Download test... \n')
        # self.dump_cookies()
        # self.load_cookies()
        time.sleep(300)
