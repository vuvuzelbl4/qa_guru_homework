import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Запуск браузера Chrome
driver = webdriver.Chrome()

try:
    # 2. Открытие страницы
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(3)  # Пауза, чтобы визуально заметить открытие

    # 3. Поиск элементов и заполнение полей
    # Находим поле Full Name по его ID и вводим текст
    full_name_field = driver.find_element(By.ID, "userName")
    full_name_field.send_keys("Иван Колбасенко")

    # Находим поле Email по его ID и вводим текст
    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("ivankolbasenko@example.com")

    #Находим поле Current Addres по его ID и заполняем
    currentAddress_field = driver.find_element(By.ID, "currentAddress")
    currentAddress_field.send_keys("Улица Пушкина, дом Колотушкина")

    #Находим поле Permanent Address по его ID и заполняем
    permanentAddress_field = driver.find_element(By.ID, "permanentAddress")
    permanentAddress_field.send_keys("Красная площадь")

    # Находим кнопку Submit по ее ID и кликаем
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 4. Проверка результата
    time.sleep(3)  # Пауза, чтобы увидеть результат отправки

    # Находим блок с отправленными данными
    result_box = driver.find_element(By.ID, "output")

    # Проверяем, что в блоке результата появился введенный текст
    assert "Красная площадь" in result_box.text
    print("Тест успешно пройден!")

finally:
    # 5. Закрытие браузера в любом случае
    driver.quit()


#ТЕСТ1 на валидность вводимого email
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(3)

    # 1. Ввод валидных данных в других полях
    driver.find_element(By.ID, "userName").send_keys("Петр Петрович")
    driver.find_element(By.ID, "currentAddress").send_keys("Улица в городе Н")
    driver.find_element(By.ID, "permanentAddress").send_keys("Валидный текст")

    # 2. Ввод НЕвалидного email
    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("ivankolbasenkoexample.com")  # Ошибка: нет @

    # 3. Нажимаем кнопку
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    time.sleep(5)  # Пауза, чтобы увидеть результат отправки

    # 4. Проверка
    result_box = driver.find_element(By.ID, "output")

    # Если email есть в результате - значит проверка не пройдена
    if "ivankolbasenkoexample.com" in result_box.text:
        print("Поздравляю! У вас не работает валидация")
    else:
        print("Неверный email попробуйте еще раз")


finally:
    driver.quit()


#ТЕСТ2 на валидность вводимого email
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(3)

    # 1. Ввод валидных данных в других полях
    driver.find_element(By.ID, "userName").send_keys("Дим Димыч")
    driver.find_element(By.ID, "currentAddress").send_keys("Станица Н")
    driver.find_element(By.ID, "permanentAddress").send_keys("Валидный супертекст")

    # 2. Ввод НЕвалидного email
    email_field = driver.find_element(By.ID, "userEmail")
    email_field.send_keys("ivankolbasenkoexample"*300+"@yandex.ru")  # Ошибка: сликшом много символов

    # 3. Нажимаем кнопку
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    time.sleep(5)  # Пауза, чтобы увидеть результат отправки

    # 4. Проверка
    result_box = driver.find_element(By.ID, "output")

    # Если email есть в результате - значит проверка не пройдена
    if "ivankolbasenkoexample@yandex.ru" in result_box.text:
        print("Поздравляю! У вас не работает валидация")
    else:
        print("Слишком много символов")


finally:
    driver.quit()