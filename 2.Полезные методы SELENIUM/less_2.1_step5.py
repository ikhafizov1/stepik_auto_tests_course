from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # функция calc, получает результат по формуле.
    def calc(x):
          return str(math.log(abs(12*math.sin(int(x)))))

    # находим значение X на странице, и получаем результат математической формулы

    x_element = browser.find_element(By.CSS_SELECTOR, ".nowrap+#input_value")
    x = x_element.text
    y = calc(x)

    # находим поле для ввода ответа и вставляем ответ в это поле

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
