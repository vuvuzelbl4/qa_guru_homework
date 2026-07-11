from pages.text_box_page import TextBoxPage


def test_text_box_form_submission(driver):
    text_box_page = TextBoxPage(driver)
    text_box_page.open()

    test_name = "Товарищ пользователь"
    test_email = "efvevee@mail.ru"
    test_current_addr = "Москва, ул.Красная площадь 1"
    test_perm_addr = "Москва, ул. Мира 2"

    text_box_page.fill_and_submit(
        name=test_name,
        email=test_email,
        current_addr=test_current_addr,
        perm_addr=test_perm_addr
    )

    assert text_box_page.is_output_visible(), "Output блок не появился после отправки формы"
    assert text_box_page.get_output_name() == test_name, f"Имя не совпадает: ожидалось '{test_name}'"
    assert text_box_page.get_output_email() == test_email, f"Email не совпадает: ожидалось '{test_email}'"
    assert text_box_page.get_output_current_address() == test_current_addr, f"Текущий адрес не совпадает"
    assert text_box_page.get_output_permanent_address() == test_perm_addr, f"Постоянный адрес не совпадает"
