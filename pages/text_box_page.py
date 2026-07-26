from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.ui import WebDriverWait


class TextBoxPage:
    URL = "https://qa-guru.github.io/one-page-form/text-box.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.output_wait = WebDriverWait(driver, 5)
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
        return self

    def _send_keys(self, locator, text):
        element = self.wait.until(es.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def enter_full_name(self, name):
        self.wait.until(es.visibility_of_element_located(self.FULL_NAME_INPUT)).send_keys(name)

    def enter_email(self, email):
        self.wait.until(es.visibility_of_element_located(self.EMAIL_INPUT)).send_keys(email)

    def fill_addresses(self, current_addr, perm_addr):
        self._send_keys(self.CURRENT_ADDRESS_INPUT, current_addr)
        self._send_keys(self.PERMANENT_ADDRESS_INPUT, perm_addr)

    def click_submit(self):
        self.wait.until(es.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def fill_and_submit(self, name, email, current_addr, perm_addr):
        self.enter_full_name(name)
        self.enter_email(email)
        self.fill_addresses(current_addr, perm_addr)
        self.click_submit()
        return self

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

    def get_raw_output_name(self) -> str:
        self.output_wait.until(es.visibility_of_element_located(self.OUTPUT_BLOCK))
        element = self.driver.find_element(*self.OUTPUT_NAME)
        full_text = element.get_attribute("textContent")
        return full_text.replace("Name:", "", 1)
