import pytest

from pages.text_box_page import TextBoxPage


class TestTextBoxForm:

    @pytest.mark.parametrize(
        "name, email, current_addr, perm_addr, expected_success",
        [
            ("Иван Иванов", "ivan@test.com", "Москва, Красная площадь 1", "Москва, Мира 2", True),
            ("", "empty@test.com", "Москва, Зеленая 22", "Минск, Независимости 12", True),
            ("Петр", "", "Москва, Краснопресненская 4", "Нижний Новгород, Ленина 8", True),
        ]
    )
    def test_text_box_form_submission(self, driver, name, email, current_addr, perm_addr, expected_success):
        page = TextBoxPage(driver).open()
        page.fill_and_submit(
            name=name,
            email=email,
            current_addr=current_addr,
            perm_addr=perm_addr
        )

        assert page.is_output_visible() is expected_success, "Output блок не появился после отправки формы"
        if expected_success:
            assert page.get_output_name() == name, f"Имя не совпадает: ожидалось '{name}'"
            assert page.get_output_email() == email, f"Email не совпадает: ожидалось '{email}'"
            assert page.get_output_current_address() == current_addr, "Текущий адрес не совпадает"
            assert page.get_output_permanent_address() == perm_addr, "Постоянный адрес не совпадает"

    class TestTextBoxSpecialCharacters:

        @pytest.mark.parametrize(
            "test_name, test_value",
            [
                ("кириллица", "Иванов Иван Иванович"),
                ("иероглифы", "测试数据"),
                ("CAPS_LOCK", "ИВАНОВ ИВАН ИВАНОВИЧ"),
            ]
        )
        def test_special_characters_in_name(self, driver, test_name, test_value):
            page = TextBoxPage(driver).open()
            page.enter_full_name(test_value)
            page.enter_email("test@test.com")
            page.fill_addresses("addr1", "addr2")
            page.click_submit()

            if page.is_output_visible():
                actual = page.get_raw_output_name()
                assert actual == test_value, (
                    f"Сценарий '{test_name}': "
                    f"ожидалось '{test_value}', получено '{actual}'"
                )
