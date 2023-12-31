import time
import allure
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from faker import Faker

from utilities.logger import Logger


class Client_information_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"


    """Getters"""

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))


    """Actions"""

    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("Input User Name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input Last Name")

    def input_postal_code(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Input Postal Code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("CLick Continue Button")


    """Methods"""

    def client_information(self):
        with allure.step("Client Information"):
            Logger.add_start_step(method='client_information')
            fake = Faker("ru_RU")
            self.get_current_url()
            self.input_first_name(fake.first_name())
            self.input_last_name(fake.last_name())
            self.input_postal_code(fake.postcode())
            self.click_continue_button()
            Logger.add_end_step(url=self.driver.current_url, method='client_information')


