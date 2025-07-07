from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    # Открываем браузер по указанной ссылке
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
          return str(math.log(abs(12*math.sin(int(x)))))

    # Находим элемент X и считаем математическую функцию при помощи def calc
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Скроллим браузер 
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("window.scrollBy(0, 150);")

    # Вставляем полученное значение в поле
    y_element = browser.find_element(By.CSS_SELECTOR, "#answer")
    y_element.send_keys(y)

    # находим и ставим галку в checkbox
    
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    # находим и ставим метку в radiobutton

    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
