from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    # Открываем браузер по указанной ссылке
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем поля Имя, Фамилия, email
    name_input = browser.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Ivan")
    lastname_input = browser.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Petrov")
    email_input = browser.find_element(By.XPATH, "//input[@name='email']").send_keys("zeroq@bin.com")

    # Загружаем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    element = browser.find_element(By.CSS_SELECTOR, "#file")    # Находим кнопку на странице по ID file
    element.send_keys(file_path)        # Добавляем файл
    
    # Нажать кнопку отправить
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
