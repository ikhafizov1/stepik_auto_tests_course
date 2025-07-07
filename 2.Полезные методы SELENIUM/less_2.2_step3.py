from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим num1 и num2, найденное переводим в текст
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    

    # Получаем сумму двух чисел переводя строковые данные в числовые
    sum_2_num = int(num1) + int(num2)

    # Находим поле для вставки суммы двух чисел.
    dropdown = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))

    # Находим из всплывающего списка вычисленное значение. Обязательно переводим сумму
    # в строковое значение.
    dropdown.select_by_value(str(sum_2_num)) 

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
