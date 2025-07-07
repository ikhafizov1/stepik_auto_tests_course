from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    # Открываем браузер по указанной ссылке
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Находим кнопку по CLASS и кликаем
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()  

    # В открывшемся всплывающем окне нажимаем ОК (исп. confirm, есть и другие) 
    confirm = browser.switch_to.alert
    confirm.accept()
    
    # Находим значение x на странице и применяем для вычисления в формуле
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x_element)

    # Вставляем полученное значение в поле
    field = browser.find_element(By.ID, "answer").send_keys(y)

    # Нажимаем кнопку для отправки формы
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Выводим полученное число в сплывающем окне в консоль CMD
    print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
