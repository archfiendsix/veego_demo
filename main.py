
from selenium import webdriver
from dotenv import load_dotenv
# from selenium.webdriver.common.keys import Keys
import urllib3
import json
import os
import unittest

import logging
import urllib3
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from pages.youtube_page import YoutubePage
from pages.telemetry import Telemetry
# from selenium.webdriver import Remote


class TelemetryTest(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.driver = webdriver.Chrome(
            executable_path="./drivers/chromedriver")
        logging.basicConfig(level=logging.INFO,
                            format='%(levelname)s : %(message)s',
                            handlers=[logging.StreamHandler()])
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        with open("config.json", "r") as json_file:
            self.config_data = json.load(json_file)

        self.youtubepage = YoutubePage(self.driver)
        self.telemetry = Telemetry(self.driver, self.config_data, 'Youtube')

    def test_telemetry(self):
        self.youtubepage.run_youtube()
        self.telemetry.run_telemetry()
        self.telemetry.run_telemetry_test()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
