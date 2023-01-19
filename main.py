
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import urllib3
import json
import os
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from pages.youtube_page import YoutubePage
from pages.telemetry import Telemetry
# from selenium.webdriver import Remote

driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
with open("config.json", "r") as json_file:
    config_data = json.load(json_file)
youtubepage = YoutubePage(driver)
telemetry = Telemetry(driver,config_data, 'Youtube')
telemetry.setup()



youtubepage.run_youtube()
telemetry.run_telemetry()
telemetry.run_telemetry_test()


