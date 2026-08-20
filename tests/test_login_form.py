import allure

from pages.login_form_page import LoginPage


@allure.epic("Форма авторизации")
@allure.feature("Валидация полей ввода")
class TestLoginForm:
    @allure.story("Отсутствует пароль")
    @allure.title("При вводе email без пароля отображается ошибка 'Password is required'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_without_password(self, driver):
        login_page = LoginPage(driver)
        with allure.step("Открываем страницу"):
            login_page.open()
        with allure.step("Пытаемся войти без пароля"):
            login_page.login(username="ehvebvjvkeve.com", password=" ")
        with allure.step("Проверяем сообщение об ошибке"):
            error_text = login_page.get_error_message_text()
        assert "Password is required" in error_text, f"Ожидалась ошибка о пароле, но получено: '{error_text}'"

    @allure.story("Отсутствует логин")
    @allure.title("При пустом логине отображается ошибка 'Login is required'")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_without_login(self, driver):
        login_page = LoginPage(driver)
        with allure.step("Открываем страницу"):
            login_page.open()
        with allure.step("Пытаемся войти без логина"):
            login_page.login(username='', password="password123")
        with allure.step("Проверяем сообщение об ошибке"):
            error_text = login_page.get_error_message_text()
        assert "Login is required" in error_text, f"Ожидалась ошибка о логине, но получено: '{error_text}'"
