from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    # Открываем браузер по указанной ссылке
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Находим кнопку на странице и кликаем по ней
    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()

    # Переходим в новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Находим значение x на странице и применяем для вычисления в формуле
    # browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(browser.find_element(By.CSS_SELECTOR, "#input_value").text)

    # Вставляем полученное значение в поле
    browser.find_element(By.ID, "answer").send_keys(y)

    # Нажимаем кнопку для отправки формы
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    
    # Выводим полученное число в сплывающем окне в консоль CMD
    print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
