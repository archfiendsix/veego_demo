
import logging
import urllib3
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.action_chains import ActionChains

import os


class BasePage:
    def __init__(self, driver):
        self.driver = driver,
        self.env_username = os.getenv("USERNAME"),
        self.env_password = os.getenv("PASSWORD")

    def setup(self):
        # load_dotenv()
        # logging.basicConfig(level=logging.INFO,
        #                     format='%(levelname)s : %(message)s',
        #                     handlers=[logging.StreamHandler()])
        # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        pass

    def logger(self, text):
        logging.info(text)
