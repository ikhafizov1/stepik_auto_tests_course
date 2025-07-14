import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
   # browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

'''
@pytest.fixture(scope="session")
def test_login(browser):
    link = "https://stepik.org/lesson/236895/step/1?auth=login"
    browser.get(link)
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(login)
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(pwd)
    browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()    
'''
