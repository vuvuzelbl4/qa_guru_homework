import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginForm:

    _LOGIN_INPUT    = (By.ID, "login-input")
    _PASSWORD_INPUT = (By.ID, "password-input")
    _SUBMIT_BUTTON  = (By.ID, "submit-button")
    _STATUS_MESSAGE = (By.ID, "error-message")


    def get_driver(self):
        return self.__driver


    def set_up(self):
        self.__driver = webdriver.Chrome()
        self.__driver.get("https://qa-guru.github.io/one-page-form/login.html")
        self.get_driver().maximize_window()

    def teardown(self):
        self.get_driver().quit()

    def test_without_password (self):
        try:
            self.set_up()

            self.get_driver().find_element(*self._LOGIN_INPUT).send_keys("ehvebvjvkeve.com")
            self.get_driver().find_element(*self._PASSWORD_INPUT).send_keys("")
            self.get_driver().find_element(*self._SUBMIT_BUTTON).click()
            error_message = self.get_driver().find_element(*self._STATUS_MESSAGE).text

            assert "Password is required (minimum 6 characters)" in error_message
            print("Тест пройден успешно!")

        finally:
            self.teardown()

    def test_without_login(self):
        try:
            self.set_up()

            self.get_driver().find_element(*self._LOGIN_INPUT).send_keys("")
            self.get_driver().find_element(*self._PASSWORD_INPUT).send_keys("password123")
            self.get_driver().find_element(*self._SUBMIT_BUTTON).click()
            error_message = self.get_driver().find_element(*self._STATUS_MESSAGE).text

            assert "Login is required (minimum 3 characters)" in error_message
            print("Тест пройден успешно!")

        finally:
            self.teardown()



