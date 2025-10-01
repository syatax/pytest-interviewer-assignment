from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DemoPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://playwright.dev"
        self.main_heading_locator = (By.CSS_SELECTOR, "h1")
        self.get_started_button_locator = (By.CSS_SELECTOR, "a[href='/docs/intro']")
        self.search_input = (By.CSS_SELECTOR, "input[placeholder='Search']")
        self.navigation_menu = (By.CSS_SELECTOR, "nav")

    def load(self):
        self.driver.get(self.url)

    def wait_for_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def has_main_heading(self):
        try:
            self.wait_for_element(self.main_heading_locator)
            return True
        except:
            return False

    def has_get_started_button(self):
        try:
            self.wait_for_element(self.get_started_button_locator)
            return True
        except:
            return False

    def main_heading(self):
        return self.driver.find_element(*self.main_heading_locator)

    def get_started_button(self):
        return self.driver.find_element(*self.get_started_button_locator)

    def wait_until_get_started_button_visible(self):
        self.wait_for_element(self.get_started_button_locator)

    def get_main_heading_text(self):
        self.wait_for_element(self.main_heading_locator)
        return self.driver.find_element(*self.main_heading_locator).text

    def click_get_started(self):
        self.wait_for_element(self.get_started_button_locator)
        self.driver.find_element(*self.get_started_button_locator).click()

    def search_for(self, query):
        self.wait_for_element(self.search_input)
        search_box = self.driver.find_element(*self.search_input)
        search_box.clear()
        search_box.send_keys(query)
        search_box.submit()

    def has_navigation_menu(self):
        self.wait_for_element(self.navigation_menu)
        return bool(self.driver.find_elements(*self.navigation_menu))