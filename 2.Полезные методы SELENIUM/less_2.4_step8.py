from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    # Открываем браузер по указанной ссылке
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Настраиваем ожидание в 12 сек и ждем прайс на дом в 100$ (динамически меняющийся прайс)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
    # Находим кнопку BOOK для клика при достижении 100$
    browser.find_element(By.CSS_SELECTOR, "#book").click()

    # Находим значение x на странице и применяем для вычисления в формуле
    y = calc(browser.find_element(By.CSS_SELECTOR, "#input_value").text)

    # Вставляем полученное значение в поле
    browser.find_element(By.ID, "answer").send_keys(y)

    # Нажимаем кнопку для отправки формы
    browser.find_element(By.CSS_SELECTOR, "#solve").click()
    
    # Выводим полученное число в сплывающем окне в консоль CMD
    print(browser.switch_to.alert.text.split(': ')[-1])

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
