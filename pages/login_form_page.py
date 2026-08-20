import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.ui import WebDriverWait


@allure.epic("Форма авторизации")
@allure.feature("Страница логина")
class LoginPage:
    URL = "https://qa-guru.github.io/one-page-form/login.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.LOGIN_INPUT = (By.ID, "login-input")
        self.PASSWORD_INPUT = (By.ID, "password-input")
        self.SUBMIT_BUTTON = (By.ID, "submit-button")
        self.ERROR_MESSAGE = (By.ID, "error-message")

    @allure.step("Открываем страницу логина")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Выполняем вход с логином '{username}' и паролем")
    def login(self, username: str, password: str):
        with allure.step(f"Вводим логин: {username}"):
            self.wait.until(es.visibility_of_element_located(self.LOGIN_INPUT)).send_keys(username)
        with allure.step("Вводим пароль"):
            self.wait.until(es.visibility_of_element_located(self.PASSWORD_INPUT)).send_keys(password)
        with allure.step("Нажимаем кнопку Submit"):
            self.wait.until(es.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    @allure.step("Проверяем видимость сообщения об ошибке")
    def is_error_visible(self) -> bool:
        try:
            self.wait.until(es.visibility_of_element_located(self.ERROR_MESSAGE))
            return True
        except TimeoutException:
            return False

    @allure.step("Получаем текст сообщения об ошибке")
    def get_error_message_text(self) -> str:
        try:
            element = self.wait.until(es.visibility_of_element_located(self.ERROR_MESSAGE))
            return element.text
        except TimeoutException:
            return " "
