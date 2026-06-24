import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es


class TestAutomationForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)
        self.url = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"

    def test_fill_entire_form(self):
        driver = self.driver
        wait = self.wait
        driver.get(self.url)

        form_title = self.wait.until(es.visibility_of_element_located((By.XPATH, "/html/body/main/section/h1")))
        self.assertEqual(form_title.text, "Practice Form")
        form_sub_title = self.wait.until(es.visibility_of_element_located((By.XPATH, "/html/body/main/section/div/p")))
        self.assertEqual(form_sub_title.text, "Student Registration Form")

        wait.until(es.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Level up your automation')]")))
        close_banner_btn = wait.until(es.element_to_be_clickable((By.XPATH, """//*[@id="fixedban"]/div/div/button""")))
        close_banner_btn.click()
        wait.until(es.invisibility_of_element(close_banner_btn))
        # Name
        first_name = self.wait.until(es.element_to_be_clickable((By.XPATH, """//*[@id="firstName"]""")))
        first_name.send_keys("Лариса")
        last_name = self.wait.until(es.element_to_be_clickable((By.XPATH, """//*[@id="lastName"]""")))
        last_name.send_keys("Иванова")
        # Email
        email = self.wait.until(es.element_to_be_clickable((By.XPATH, """//*[@id="userEmail"]""")))
        email.send_keys("larisa_ivanova@mail.com")
        # Gender
        gender_male_label = self.wait.until(
            es.element_to_be_clickable((By.CSS_SELECTOR, "label[for='gender-radio-1']")))
        gender_male_label.click()
        # Mobile
        mobile_number = self.wait.until(es.element_to_be_clickable((By.XPATH, """//*[@id="userNumber"]""")))
        mobile_number.send_keys("9265520357")
        # Date of Birth
        date_input = self.wait.until(es.element_to_be_clickable((By.XPATH, """//*[@id="dateOfBirthInput"]""")))
        date_input.click()
        self.wait.until(es.visibility_of_element_located((By.CLASS_NAME, "react-datepicker__month-container")))
        month_select = self.wait.until(es.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select")))
        month_select.click()
        month_select.find_element(By.XPATH, "//option[@value='3']").click()
        year_select = driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
        year_select.click()
        year_select.find_element(By.XPATH, "//option[@value='2000']").click()
        day_element = driver.find_element(By.CSS_SELECTOR,
                                          ".react-datepicker__day--012:not(.react-datepicker__day--outside-month)")
        day_element.click()
        # Subjects
        subjects_input = self.wait.until(es.element_to_be_clickable((By.XPATH, """//*[@id="subjectsInput"]""")))
        subjects_input.send_keys("Computer Science")
        subjects_input.send_keys(Keys.ENTER)
        # Hobbies
        hobby_sports = self.wait.until(es.element_to_be_clickable((By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")))
        hobby_sports.click()
        # Picture
        temp_file_path = os.path.abspath("test_image.jpg")
        with open(temp_file_path, "w") as f:
            f.write("fake image data")

        upload_input = self.wait.until(es.element_to_be_clickable((By.XPATH, """//*[@id="uploadPicture"]""")))
        upload_input.send_keys(temp_file_path)
        # Current Address
        current_address = self.wait.until(es.element_to_be_clickable((By.XPATH, """//*[@id="currentAddress"]""")))
        current_address.send_keys("г.Москва, ул.Преображенская площадь, д.4")
        # Scroll
        state_dropdown = driver.find_element(By.ID, "state")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", state_dropdown)
        state_dropdown.click()
        # State and City
        state_dropdown = self.wait.until(es.element_to_be_clickable((By.XPATH, """//*[@id="state"]""")))
        state_dropdown.click()
        state_option = self.wait.until(
            es.element_to_be_clickable((By.XPATH, """//*[@id="stateCity-wrapper"]/div[1]""")))
        state_option.click()
        city_dropdown = self.wait.until(es.element_to_be_clickable((By.XPATH, """//*[@id="city"]""")))
        city_dropdown.click()
        city_option = self.wait.until(es.element_to_be_clickable((By.XPATH, """//*[@id="stateCity-wrapper"]/div[1]""")))
        city_option.click()
        # Submit
        submit_button = self.wait.until(es.element_to_be_clickable((By.XPATH, """//*[@id="submit"]""")))
        submit_button.click()
        # Expected Conditions
        modal_title = self.wait.until(
            es.element_to_be_clickable((By.XPATH, """//*[@id="example-modal-sizes-title-lg"]""")))
        self.assertEqual(modal_title.text, "Thanks for submitting the form")

        result_table = driver.find_element(By.CLASS_NAME, "table-responsive")
        self.assertIn("Лариса Иванова", result_table.text)
        self.assertIn("larisa_ivanova@mail.com", result_table.text)
        self.assertIn("Male", result_table.text)
        self.assertIn("9265520357", result_table.text)
        self.assertIn("12 Apr 2000", result_table.text)
        self.assertIn("Computer Science", result_table.text)
        self.assertIn("Sports", result_table.text)
        self.assertIn("test_image.jpg", result_table.text)
        self.assertIn("г.Москва, ул.Преображенская площадь, д.4", result_table.text)
        self.assertIn("NCR Delhi", result_table.text)

    def tearDown(self):
        if os.path.exists("test_image.jpg"):
            os.remove("test_image.jpg")
        self.driver.quit()
