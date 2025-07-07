import os
import math # Only if a quiz is involved, not directly in this registration test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, AssertionError, NoAlertPresentException

# --- Core Page Object Classes ---

class BasePage:
    """
    Base class for all Page Objects, providing common browser interactions.
    """
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """Navigates the browser to the specified URL."""
        self.driver.get(self.url)

    def find_element(self, by_locator, timeout=10):
        """
        Waits for and finds a single web element.
        Raises TimeoutException if element not found within timeout.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(by_locator)
            )
        except TimeoutException:
            raise NoSuchElementException(f"Element not found within {timeout} seconds: {by_locator}")

    def get_element_text(self, by_locator, timeout=10):
        """Waits for element visibility and returns its text."""
        element = self.find_element(by_locator, timeout)
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of(element)
        )
        return element.text

    def take_screenshot(self, filename="error_screenshot.png"):
        """Captures a screenshot of the current browser state."""
        screenshot_path = os.path.join(os.getcwd(), filename)
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")

class RegistrationPage(BasePage):
    """
    Page Object for the user registration form.
    Defines locators and interaction methods specific to this page.
    """
    # Locators for elements on the registration page
    _FIRST_NAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Input your first name"][required]')
    _LAST_NAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Input your last name"][required]')
    _EMAIL_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Input your email"][required]')
    _SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn")
    _SUCCESS_MESSAGE_HEADER = (By.TAG_NAME, "h1")

    def __init__(self, driver):
        super().__init__(driver, "http://suninjuly.github.io/registration2.html")

    def fill_registration_form(self, first_name, last_name, email):
        """Fills out the required fields of the registration form."""
        print(f"  Attempting to fill form for {first_name} {last_name}, {email}")
        self.find_element(self._FIRST_NAME_FIELD).send_keys(first_name)
        self.find_element(self._LAST_NAME_FIELD).send_keys(last_name)
        self.find_element(self._EMAIL_FIELD).send_keys(email)
        print("  Form fields populated.")

    def submit_form(self):
        """Clicks the submit button on the registration form."""
        print("  Submitting registration form.")
        self.find_element(self._SUBMIT_BUTTON).click()

    def get_success_message(self, timeout=10):
        """
        Waits for and retrieves the success message after form submission.
        Raises TimeoutException if message doesn't appear.
        """
        print(f"  Waiting for success message (up to {timeout}s)...")
        return self.get_element_text(self._SUCCESS_MESSAGE_HEADER, timeout)

    def verify_success_message(self, expected_text):
        """Compares the actual success message with the expected one."""
        actual_message = self.get_success_message()
        print(f"  Verifying success message. Expected: '{expected_text}', Actual: '{actual_message}'")
        assert actual_message == expected_text, \
            f"Registration success message mismatch! Expected: '{expected_text}', Got: '{actual_message}'"
        print("✔ Success message verified!")

# --- Test Execution ---

def execute_registration_test():
    """
    Orchestrates the end-to-end user registration test.
    """
    print("\n--- Starting User Registration Test ---")
    # Initialize WebDriver within a 'with' block for automatic cleanup
    with webdriver.Chrome() as driver:
        # Set implicit wait, a general wait for elements to appear.
        driver.implicitly_wait(5)

        registration_page = RegistrationPage(driver)
        expected_success_text = "Congratulations! You have successfully registered!"

        try:
            # Step 1: Open the registration page
            print("1. Opening registration page...")
            registration_page.open()

            # Step 2: Fill out the registration form
            print("2. Filling out registration form...")
            registration_page.fill_registration_form("Alice", "Smith", "alice.smith@example.com")

            # Step 3: Submit the form
            print("3. Submitting the form...")
            registration_page.submit_form()

            # Step 4: Verify the success message
            print("4. Verifying success message...")
            registration_page.verify_success_message(expected_success_text)

            print("\n✅ Test Passed: User registration was successful!")

        except (NoSuchElementException, TimeoutException) as e:
            print(f"\n❌ Test Failed: A required element was not found or timed out. Error: {e}")
            registration_page.take_screenshot("registration_error.png")
        except AssertionError as e:
            print(f"\n❌ Test Failed: Assertion mismatch. Error: {e}")
            registration_page.take_screenshot("assertion_failed.png")
        except Exception as e:
            print(f"\n❌ Test Failed: An unexpected error occurred. Error: {e}")
            registration_page.take_screenshot("unexpected_error.png")
        finally:
            print("\n--- Test Run Concluded ---")
            time.sleep(3) # Short pause to observe final state before closing

# --- Main Execution Point ---
if __name__ == "__main__":
    execute_registration_test()
