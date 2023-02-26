import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class MicrosoftPage(BasePage):
    def __init__(self, driver, test_sites):     
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.test_sites = test_sites
        self.timeout = 10

   

    def run_microsoft_download(self, timeout=180):
        
        self.driver.get(self.test_sites["microsoft_download"])
        
        
        self.logger(f'\nStarting Microsoft download test... \n')

        wait = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.ID, 'product-edition'))
        )

        wait = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.ID, 'submit-product-edition'))
        )
        product_select = Select(self.driver.find_element(By.ID, 'product-edition'))
        product_download_btn = self.driver.find_element(By.ID, 'submit-product-edition')
        product_select.select_by_visible_text("Windows 11 (multi-edition ISO for x64 devices)")
        product_download_btn.click()
        wait = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.ID, 'product-languages'))
        )
        wait = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.ID, 'submit-sku'))
        )
        product_language_select = Select(self.driver.find_element(By.ID, 'product-languages'))
        confirm_language_btn = self.driver.find_element(By.ID, 'submit-sku')
        product_language_select.select_by_visible_text("English International")
        confirm_language_btn.click()

        wait = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="card-info-content"]/div/div/div/a'))
        )
        final_download_btn = self.driver.find_element(By.XPATH, '//*[@id="card-info-content"]/div/div/div/a')
        final_download_btn.click()
        self.logger(f'\nMicrosoft download started... \n')
        time.sleep(timeout)

   