from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time # Все еще нужен для окончательной задержки, если хочется увидеть результат

def test_user_registration_form():
    # Используем 'with' для автоматического закрытия браузера
    with webdriver.Chrome() as driver:
        # Установим неявное ожидание. Это поможет драйверу подождать,
        # если элементы загружаются не мгновенно.
        driver.implicitly_wait(5) # Ждем до 5 секунд для появления элемента

        try:
            # Переход на веб-страницу
            driver.get("http://suninjuly.github.io/registration2.html")

            # Заполнение обязательных полей формы
            # Используем более точные CSS-селекторы, т.к. XPATH по placeholder менее надежен
            # и может быть медленнее. К тому же, есть атрибут 'required'.
            driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"][required]').send_keys("Ivan")
            driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"][required]').send_keys("Petrov")
            driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"][required]').send_keys("test@test.com")

            # Клик по кнопке отправки формы
            submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
            submit_button.click()

            # Явное ожидание появления сообщения об успехе
            # Ждем до 10 секунд, пока элемент <h1> с нужным текстом не станет видимым
            success_message_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.TAG_NAME, "h1"))
            )
            success_message_text = success_message_element.text

            # Проверка результата
            assert "Congratulations! You have successfully registered!" == success_message_text, \
                f"Ожидаемое сообщение не совпадает. Ожидали: 'Congratulations! You have successfully registered!', получили: '{success_message_text}'"

            print("Тест успешно пройден: Пользователь зарегистрирован!")
            time.sleep(3) # Небольшая задержка, чтобы увидеть результат перед закрытием

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Тест провалился из-за ошибки элемента или ожидания: {e}")
            # Можно сделать скриншот для отладки
            # driver.save_screenshot("error_screenshot.png")
        except AssertionError as e:
            print(f"Тест провалился из-за неверного сообщения: {e}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

# Точка входа для запуска
if __name__ == "__main__":
    test_user_registration_form()
