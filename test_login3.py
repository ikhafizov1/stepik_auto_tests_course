import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

login = ""
pwd = ""
#answer = math.log(int(time.time() - 0.037))

@pytest.mark.parametrize('links',
                         ["https://stepik.org/lesson/236895/step/1?auth=login",
                          "https://stepik.org/lesson/236896/step/1?auth=login",
                          "https://stepik.org/lesson/236897/step/1?auth=login",
                          "https://stepik.org/lesson/236898/step/1?auth=login",
                          "https://stepik.org/lesson/236899/step/1?auth=login",
                          "https://stepik.org/lesson/236903/step/1?auth=login",
                          "https://stepik.org/lesson/236904/step/1?auth=login",
                          "https://stepik.org/lesson/236905/step/1?auth=login"]
                         )
def test_login(browser, links):
    link = f"{links}"
    browser.get(link)
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(login)
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(pwd)
    browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()
    time.sleep(5)
    browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea").send_keys(math.log(int(time.time() - 0.037)))
    time.sleep(10)
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    time.sleep(10)
    answer_ = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert answer_ == 'Correct!', 'Something wrong, is not correct value'
    browser.find_element(By.CLASS_NAME, "again-btn.white").click()
    time.sleep(15)
