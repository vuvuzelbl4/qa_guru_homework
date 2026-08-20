import allure
import pytest

from pages.text_box_page import TextBoxPage


@allure.epic("Форма TextBox")
@allure.feature("Отправка формы с разными данными")
class TestTextBoxForm:

    @allure.story("Валидация заполнения полей")
    @allure.title("Отправка формы с параметрами: name='{name}', email='{email}'")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "name, email, current_addr, perm_addr, expected_success",
        [
            pytest.param("Иван Иванов", "ivan@test.com", "Москва, Красная площадь 1", "Москва, Мира 2", True,
                         id="Полные данные"),
            pytest.param("", "empty@test.com", "Москва, Зеленая 22", "Минск, Независимости 12", True,
                         id="Пустое имя"),
            pytest.param("Петр", "", "Москва, Краснопресненская 4", "Нижний Новгород, Ленина 8", True,
                         id="Пустой email"),
        ]
    )
    def test_text_box_form_submission(self, driver, name, email, current_addr, perm_addr, expected_success):
        allure.attach(
            f"Name: {name}\nEmail: {email}\nCurrent: {current_addr}\nPermanent: {perm_addr}",
            name="Входные данные",
            attachment_type=allure.attachment_type.TEXT
        )
        page = TextBoxPage(driver).open()
        with allure.step("Заполняем форму и отправляем"):
            page.fill_and_submit(
                name=name,
                email=email,
                current_addr=current_addr,
                perm_addr=perm_addr
            )

        with allure.step("Проверяем результат"):
            assert page.is_output_visible() is expected_success, "Output блок не появился после отправки формы"

            if expected_success:
                with allure.step("Сравниваем заполненные данные с результатом"):
                    actual_name = page.get_output_name()
                    actual_email = page.get_output_email()
                    actual_current = page.get_output_current_address()
                    actual_perm = page.get_output_permanent_address()
                    allure.attach(
                        f"Name: '{actual_name}' (ожидалось '{name}')\n"
                        f"Email: '{actual_email}' (ожидалось '{email}')\n"
                        f"Current: '{actual_current}'\n"
                        f"Permanent: '{actual_perm}'",
                        name="Результат сравнения",
                        attachment_type=allure.attachment_type.TEXT
                    )
                    assert actual_name == name, f"Имя не совпадает: ожидалось '{name}', получено '{actual_name}'"
                    assert actual_email == email, f"Email не совпадает: ожидалось '{email}', получено '{actual_email}'"
                    assert actual_current == current_addr, f"Текущий адрес не совпадает: ожидалось '{current_addr}'"
                    assert actual_perm == perm_addr, f"Постоянный адрес не совпадает: ожидалось '{perm_addr}'"

    @allure.epic("Форма TextBox")
    @allure.feature("Специальные символы")
    class TestTextBoxSpecialCharacters:

        @allure.story("Поддержка различных кодировок и регистров")
        @allure.title("Ввод специальных символов: {test_name}")
        @allure.severity(allure.severity_level.NORMAL)
        @pytest.mark.parametrize(
            "test_name, test_value",
            [
                pytest.param("кириллица", "Иванов Иван Иванович", id="Русские буквы"),
                pytest.param("иероглифы", "测试数据", id="Китайские иероглифы"),
                pytest.param("CAPS_LOCK", "ИВАНОВ ИВАН ИВАНОВИЧ", id="ВЕРХНИЙ РЕГИСТР"),
            ]
        )
        def test_special_characters_in_name(self, driver, test_name, test_value):
            allure.attach(
                f"Тип теста: {test_name}\nЗначение: {test_value}",
                name="Тестовые данные",
                attachment_type=allure.attachment_type.TEXT
            )

            page = TextBoxPage(driver).open()

            with allure.step("Заполняем форму специальными символами"):
                page.enter_full_name(test_value)
                page.enter_email("test@test.com")
                page.fill_addresses("addr1", "addr2")
                page.click_submit()

            with allure.step("Проверяем результат"):
                if page.is_output_visible():
                    actual = page.get_raw_output_name()
                    allure.attach(
                        f"Ожидалось: '{test_value}'\nПолучено: '{actual}'",
                        name="Сравнение значений",
                        attachment_type=allure.attachment_type.TEXT
                    )
                    assert actual == test_value, (
                        f"Сценарий '{test_name}': "
                        f"ожидалось '{test_value}', получено '{actual}'"
                    )
