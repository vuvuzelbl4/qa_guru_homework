from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    URL = "https://qa-guru.github.io/one-page-form/login.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.LOGIN_INPUT = (By.ID, "login-input")
        self.PASSWORD_INPUT = (By.ID, "password-input")
        self.SUBMIT_BUTTON = (By.ID, "submit-button")
        self.ERROR_MESSAGE = (By.ID, "error-message")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username: str, password: str):
        self.wait.until(es.visibility_of_element_located(self.LOGIN_INPUT)).send_keys(username)
        self.wait.until(es.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)
        self.wait.until(es.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def is_error_visible(self) -> bool:
        try:
            self.wait.until(es.visibility_of_element_located(self.ERROR_MESSAGE))
            return True
        except TimeoutException:
            return False

    def get_error_message_text(self) -> str:
        try:
            element = self.wait.until(es.visibility_of_element_located(self.ERROR_MESSAGE))
            return element.text
        except TimeoutException:
            return " "
