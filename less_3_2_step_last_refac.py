import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def fill_form(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля формы
    browser.find_element(By.CLASS_NAME, "first_block .form-control.first").send_keys("Ivan")
    browser.find_element(By.CLASS_NAME, "first_block .form-control.second").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "first_block .form-control.third").send_keys("zeroq@rambler.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст "Congratulations! You have successfully registered!"
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    return welcome_text

    # Создаем класс с тестами
class Test_Class_Form(unittest.TestCase):

    # тест первый для линка 1
    def test_link1(self):
        text_link1 = fill_form("http://suninjuly.github.io/registration1.html")
        # Проверка результата
        self.assertEqual("Congratulations! You have successfully registered!",text_link1, "Mayby have a problem")

    # тест второй для линка 2
    def test_link2(self):
        text_link2 = fill_form("http://suninjuly.github.io/registration2.html")
        # Проверка результата
        self.assertEqual("Congratulations! You have successfully registered!",text_link2, "Mayby have a problem")

           
if __name__ == "__main__":
    unittest.main()        


