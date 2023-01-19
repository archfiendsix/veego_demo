import time
import json
import logging
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class Telemetry(BasePage):
    def __init__(self, driver,config_data, name):
        super().__init__(driver)
        self.driver = driver
        self.config_data = config_data
        self.name = name

    def run_telemetry(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.config_data["telemetry"])

        time.sleep(10)
        login_texbox = self.driver.find_element(By.ID, "username")
        password_textbox = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "kc-login")

        login_texbox.send_keys(self.env_username)
        password_textbox.send_keys(self.env_password)
        login_button.click()
        time.sleep(5)

        

    def return_page_service_items(self, name, type, is_classification_final):
        body = self.driver.find_element(By.CSS_SELECTOR, "body")
        body_text = body.text

        text_to_json = json.loads(body_text)
        services = text_to_json["devices"][0]["discovery"]["devices"][self.config_data["mac"]]["services"]
        service_items = {key: value for key, value in services.items(
        ) if value["is_classification_final"] == is_classification_final and value["type"] == type and value["name"] == name}

        return service_items

    def service_final_test(self, name):
        pass
        
    
    def run_telemetry_test(self):
        
        service_item = self.return_page_service_items(
            'Youtube', 'STREAMING', True)
        try:
            assert service_item
            detection_time = datetime.utcnow()
            for key in service_item.keys():
                service_type = service_item[key]['type']
                service_name = service_item[key]['name']
                service_start_time_stamp = service_item[key]['start_time']
                service_start_time_formatted = datetime.utcfromtimestamp(
                    service_start_time_stamp/1000).strftime("%Y-%m-%d %H:%M:%S")
                service_start_time = datetime.utcfromtimestamp(
                    service_start_time_stamp/1000)
                print(f"{service_name} {service_type} started at: {service_start_time_formatted}")
        except AssertionError:
            logging.warning("Fail: No Youtube service found")

        rerun = 0
        while service_item:

            uuid_key = next(iter(service_item))
            for key in service_item.keys():

                delta = detection_time - service_start_time

                print(f'Name: {service_name}')
                print(f'Service Type: {service_type}')
                print(f'Recognized in: {delta} Minutes')
                print(f'Service UUID: {uuid_key}')

                self.service_final_test('Youtube')



            if service_type == "STREAMING" and service_name == "" or service_name == None:
                assert True
                logging.info(
                    "Partial PASS: Type is correct, name is empty")
            elif service_type == "STREAMING" and service_name != "Youtube":
                try:
                    assert False
                except AssertionError:
                    logging.warning(
                        "Fail: Type is correct, name is incorrect")
            elif service_type == "STREAMING" and service_name == "Youtube":
                logging.info("PASS: Both type and name are correct")
                assert True
            else:
                logging.info("Fail: Type and/or name are incorrect")
                assert False







            self.driver.refresh()
            service_item = False
            service_item = self.return_page_service_items(
                'Youtube', 'STREAMING', True)
            rerun = rerun+1
            if service_item:
                print(
                    f"\nRunning service recognition test again ({rerun})..\n")
            else:
                print(
                    f"\nNo Service recognized for Youtube. Retrying Service recognition Test... ({rerun})...\n")
                total_testing_time = datetime.utcnow() - detection_time
                if total_testing_time.total_seconds() >= 360:
                    total_testing_time = total_testing_time/60
                    logging.info(
                        f"No Youtube service recognized in {total_testing_time} minutes\n")
            time.sleep(10)
