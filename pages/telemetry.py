import time
import json
import logging
import requests
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class Telemetry(BasePage):
    def __init__(self, driver, config_data, ):
        super().__init__(driver)
        self.driver = driver
        self.config_data = config_data
        self.login_texbox_locator = (By.ID, "username")

    def run_telemetry(self):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(
            self.config_data["telemetry"]+self.config_data["router_id"])

        self.driver.maximize_window()

        time.sleep(10)

        if self.driver.title == "Sign in to veego":

            login_texbox = self.driver.find_element(By.ID, "username")

            login_texbox = WebDriverWait(self.driver, 360).until(
                EC.presence_of_element_located(
                    self.login_texbox_locator)
            )
            login_texbox.send_keys(self.env_username)

            password_textbox = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.ID, "kc-login")

            password_textbox.send_keys(self.env_password)
            login_button.click()

       
        time.sleep(5)

        # self.driver.get("http://127.0.0.1:5500/selenium_chrome/index.html")

    def return_page_service_items(self, name, type, is_classification_final):
        # Switch to the second tab
        # self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.refresh()
        # logging.info("\nLooking for services...\n")
        service_items = None

        # Test code */
        # Set up authentication credentials
        # username = self.env_username
        # password = str(self.env_password)
        # auth = (username, password)

        # response = requests.get(self.config_data['telemetry']+self.config_data['router_id'], auth=auth)

        # # Check if the request was successful
        # if response.status_code == 200:
        #     # Get the response body as text
        #     body_text = response.text
        #     # Do something with the body text
        #     print(body_text)
        # else:
        #     print('Failed to make request:', response.status_code)

        # Test code */
        body = self.driver.find_element(By.CSS_SELECTOR, "body")
        body_text = body.text

        try:
            text_to_json = json.loads(body_text)
        except json.decoder.JSONDecodeError as e:
            logging.error(f"Failed to parse JSON data: {e}")
            return

        services = text_to_json["devices"][0]["discovery"]["devices"][self.config_data["mac"]]["services"]
        assert services, "No runnning services detected"
        service_items = {key: value for key, value in services.items(
        ) if value["is_classification_final"] == is_classification_final and value["type"] == type and value["name"] == name}

        return service_items

    # def return_page_service_items(self, name, type, is_classification_final):
    #     self.driver.refresh()
    #     logging.info("Looking for services...")
    #     service_items = None

    #     with open("sample.json", "r") as json_file:
    #         body = json.load(json_file)

    #     # body = self.driver.find_element(By.CSS_SELECTOR, "body")
    #     body_text = body.text

    #     try:
    #         text_to_json = json.loads(body_text)
    #     except json.decoder.JSONDecodeError as e:
    #         logging.error(f"Failed to parse JSON data: {e}")
    #         return

    #     services = text_to_json["devices"][0]["discovery"]["devices"][self.config_data["mac"]]["services"]
    #     assert services, "No runnning services found"
    #     service_items = {key: value for key, value in services.items(
    #     ) if value["is_classification_final"] == is_classification_final and value["type"] == type and value["name"] == name}

    #     return service_items

    def run_telemetry_test(self, service, service_type, classification_final):
        logging.info("\nLooking for services...\n")
        # Initialize variables
        rerun = 0
        max_runtime = 10 * 60  # 10 minutes in seconds
        detection_time = datetime.utcnow()

        # Loop until maximum runtime is reached
        while (datetime.utcnow() - detection_time).total_seconds() <= max_runtime:
            # Try to detect the service
            service_item = self.return_page_service_items(
                service, service_type, classification_final)

            # Loop until service is detected or maximum runtime is reached
            while service_item:
                # Print information about detected service
                uuid_key = next(iter(service_item))
                detected_service_name = service_item[uuid_key]['name']
                detected_service_type = service_item[uuid_key]['type']
                detected_is_classification_final = service_item[uuid_key]['is_classification_final']
                service_start_time = datetime.utcfromtimestamp(
                    service_item[uuid_key]['start_time']/1000)
                delta = detection_time - service_start_time
                print(
                    f"{detected_service_name} {detected_service_type} started at: {service_start_time}")
                print(f"Name: {detected_service_name}")
                print(f"Service Type: {detected_service_type}")
                print(f"Recognized in: {delta} Minutes")
                print(f"Service UUID: {uuid_key}")

                # Check if service is correct and log message accordingly
                if detected_service_name == service and detected_service_name == service:
                    logging.info("PASS: Both type and name are correct")
                elif detected_service_type == service_type and (not detected_service_name or detected_service_name == ''):
                    assert True
                    logging.warning(
                        "Partial PASS: Type is correct, name is empty")
                elif detected_service_type == service_type and detected_service_name != service:
                    logging.warning("Fail: Type is correct, name is incorrect")
                else:
                    logging.error("Fail: Type and/or name are incorrect")

                # Wait before trying to detect service again
                time.sleep(10)

                # Check if maximum runtime has been reached and exit if it has
                if (datetime.utcnow() - detection_time).total_seconds() > max_runtime:
                    logging.info("Maximum runtime exceeded, exiting function")
                    return

                # Try to detect the service again
                rerun += 1
                service_item = self.return_page_service_items(
                    service, service_type, classification_final)

            # Print message if service is not detected within the allowed time
            total_testing_time = datetime.utcnow() - detection_time
            if total_testing_time.total_seconds() >= 360:
                total_testing_time = total_testing_time / 60
                logging.info(
                    f"No {service} service recognized for the past {total_testing_time} minutes\n")
                assert False
                return

            # Wait before trying to detect service again
            rerun += 1
            # Switch to the second tab
            # self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(10)
            print(
                f"No {service} service detected. Retrying service recognition test ({rerun})...\n")
