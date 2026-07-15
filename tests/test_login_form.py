from pages.login_form_page import LoginPage


class TestLoginForm:

    def test_without_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username="ehvebvjvkeve.com", password=" ")
        error_text = login_page.get_error_message_text()
        assert "Password is required" in error_text, f"Ожидалась ошибка о пароле, но получено: '{error_text}'"

    def test_without_login(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username='', password="password123")
        error_text = login_page.get_error_message_text()
        assert "Login is required" in error_text, f"Ожидалась ошибка о логине, но получено: '{error_text}'"
