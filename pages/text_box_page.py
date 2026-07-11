from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as es


class TextBoxPage:
    URL = "https://qa-guru.github.io/one-page-form/text-box.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.output_wait = WebDriverWait(driver, 3)
        self.FULL_NAME_INPUT = (By.ID, "userName")
        self.EMAIL_INPUT = (By.ID, "userEmail")
        self.CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
        self.PERMANENT_ADDRESS_INPUT = (By.ID, "permanentAddress")
        self.SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
        self.OUTPUT_BLOCK = (By.ID, "output")
        self.OUTPUT_NAME = (By.CSS_SELECTOR, "#output #name")
        self.OUTPUT_EMAIL = (By.CSS_SELECTOR, "#output #email")
        self.OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
        self.OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

    def open(self):
        self.driver.get(self.URL)

    def enter_full_name(self, name):
        self.wait.until(es.visibility_of_element_located(self.FULL_NAME_INPUT)).send_keys(name)

    def enter_email(self, email):
        self.wait.until(es.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)

    def fill_addresses(self, current_addr, perm_addr):
        self.driver.find_element(*self.CURRENT_ADDRESS_INPUT).send_keys(current_addr)
        self.driver.find_element(*self.PERMANENT_ADDRESS_INPUT).send_keys(perm_addr)

    def click_submit(self):
        self.wait.until(es.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def fill_and_submit(self, name, email, current_addr, perm_addr):
        self.enter_full_name(name)
        self.enter_email(email)
        self.fill_addresses(current_addr, perm_addr)
        self.click_submit()

    def get_output_name(self) -> str:
        self.output_wait.until(es.visibility_of_element_located(self.OUTPUT_BLOCK))
        full_text = self.driver.find_element(*self.OUTPUT_NAME).text
        return full_text.replace("Name:", "").strip()

    def get_output_email(self) -> str:
        self.output_wait.until(es.visibility_of_element_located(self.OUTPUT_BLOCK))
        full_text = self.driver.find_element(*self.OUTPUT_EMAIL).text
        return full_text.replace("Email:", "").strip()

    def get_output_current_address(self) -> str:
        self.output_wait.until(es.visibility_of_element_located(self.OUTPUT_BLOCK))
        full_text = self.driver.find_element(*self.OUTPUT_CURRENT_ADDRESS).text
        return full_text.replace("Current Address :", "").strip()

    def get_output_permanent_address(self) -> str:
        self.output_wait.until(es.visibility_of_element_located(self.OUTPUT_BLOCK))
        full_text = self.driver.find_element(*self.OUTPUT_PERMANENT_ADDRESS).text
        return full_text.replace("Permananet Address :", "").strip()

    def is_output_visible(self) -> bool:
        try:
            self.output_wait.until(es.visibility_of_element_located(self.OUTPUT_BLOCK))
            return True
        except TimeoutException:
            return False
