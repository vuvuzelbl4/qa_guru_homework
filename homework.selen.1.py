import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class Tests:
    def __init__(self, url):
        self.__url = url

    #Метод для получения url
    def get_url(self):
        return self.__url

    #Метод для получения driver
    def get_driver(self):
        return self.__driver

    def set_driver(self, driver):
            self.__driver = driver

    #Метод для создания нового драйвера перед каждым тестом
    def set_up(self):
        self.__driver = webdriver.Chrome()
        self.get_driver().get(self.get_url())
        self.get_driver().maximize_window()
        time.sleep(3)
    #Метод закрывающий драйвер после каждого теста
    def teardown(self):
        self.get_driver().quit()

    full_name_locator = "userName"
    email_locator = "userEmail"
    current_locator = "currentAddress"
    permanent_locator = "permanentAddress"
    submit_locator = "submit"
    result_box_locator = "output"

    def test1(self):

        try:
            self.set_up()  # Запускаем новый браузер

            # 3. Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            full_name_field = self.get_driver().find_element(By.ID,self.full_name_locator)
            full_name_field.send_keys("Иван Колбасенко")

            # Находим поле Email по его ID и вводим текст
            email_field = self.get_driver().find_element(By.ID,self.email_locator)
            email_field.send_keys("ivankolbasenko@example.com")

            #Находим поле Current Addres по его ID и заполняем
            currentAddress_field = self.get_driver().find_element(By.ID,self.current_locator)
            currentAddress_field.send_keys("Улица Пушкина, дом Колотушкина")

            #Находим поле Permanent Address по его ID и заполняем
            permanentAddress_field = self.get_driver().find_element(By.ID,self.permanent_locator)
            permanentAddress_field.send_keys("Красная площадь")

            # Находим кнопку Submit по ее ID и кликаем
            submit_button = self.get_driver().find_element(By.ID,self.submit_locator)
            submit_button.click()

            # 4. Проверка результата
            time.sleep(3)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = self.get_driver().find_element(By.ID,self.result_box_locator)

            # Проверяем, что в блоке результата появился введенный текст
            assert "Красная площадь" in result_box.text
            print("Тест1 успешно пройден!")

        finally:
            self.teardown()

    def test2(self):
        try:
            self.set_up()

            # 1. Ввод валидных данных в других полях
            self.get_driver().find_element(By.ID, self.full_name_locator ).send_keys("Петр Петрович")
            self.get_driver().find_element(By.ID, self.current_locator).send_keys("Улица в городе Н")
            self.get_driver().find_element(By.ID, self.permanent_locator).send_keys("Валидный текст")

            # 2. Ввод НЕвалидного email
            email_field = self.get_driver().find_element(By.ID, self.email_locator)
            email_field.send_keys("ivankolbasenkoexample.com")  # Ошибка: нет @

            # 3. Нажимаем кнопку
            submit_button = self.get_driver().find_element(By.ID, self.submit_locator)
            submit_button.click()
            time.sleep(3)  # Пауза, чтобы увидеть результат отправки

            # 4. Проверка
            result_box = self.get_driver().find_element(By.ID, self.result_box_locator)

            # Если email есть в результате - значит проверка не пройдена
            assert "ivankolbasenkoexample.com" not in result_box.text
            print("Тест2 успешно пройден")


        finally:
            self.teardown()

    def test3(self):
        try:
            self.set_up()

            # 1. Ввод валидных данных в других полях
            self.get_driver().find_element(By.ID, self.full_name_locator).send_keys("Дим Димыч")
            self.get_driver().find_element(By.ID, self.current_locator).send_keys("Станица Н")
            self.get_driver().find_element(By.ID, self.permanent_locator).send_keys("Валидный супертекст")

            # 2. Ввод НЕвалидного email
            email_field = self.get_driver().find_element(By.ID, self.email_locator)
            email_field.send_keys("ivankolbasenkoexample" * 300 + "@yandex.ru")  # Ошибка: сликшом много символов

            # 3. Нажимаем кнопку
            submit_button = self.get_driver().find_element(By.ID, self.submit_locator)
            submit_button.click()
            time.sleep(3)  # Пауза, чтобы увидеть результат отправки

            # 4. Проверка
            result_box = self.get_driver().find_element(By.ID, self.result_box_locator)

            # Если email есть в результате - значит проверка не пройдена
            assert len(result_box.text) < 256, "Слишком много символов!"
            print("Тест3 успешно пройден")



        finally:
            self.teardown()



# 1. Запуск браузера Chrome
url = "https://qa-guru.github.io/one-page-form/text-box.html"
test_suite = Tests(url)

test_suite.test1()
test_suite.test2()
test_suite.test3()
