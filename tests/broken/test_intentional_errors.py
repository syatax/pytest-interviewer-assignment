import pytest
from support.pages.demo_page import DemoPage
from selenium.webdriver.common.by import By
# Fixed missing lib
import requests

@pytest.fixture
def demo_page(driver):
    return DemoPage(driver)

@pytest.mark.nondestructive
def test_homepage_verification(demo_page):
    demo_page.load()
    assert demo_page.has_main_heading()
    assert demo_page.has_get_started_button()
    # Fixed point on the end of string
    assert demo_page.main_heading().text == "Playwright enables reliable end-to-end testing for modern web apps."
    demo_page.wait_until_get_started_button_visible()
    # Fixed remove ? from is_displayed
    assert demo_page.get_started_button().is_displayed()

@pytest.mark.nondestructive
def test_navigation_verification(demo_page):
    demo_page.load()
    # Fixed change default method from set to click
    demo_page.get_started_button().click()
    assert "docs" in demo_page.driver.current_url
    # Fixed () end of function call
    assert demo_page.has_get_started_button()

@pytest.mark.nondestructive
def test_api_integrations():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "New Post",
        "body": "Content",
        "userId": 1
    }
    # Fixed request method
    response = requests.post(url, json=payload)

    # Fixed status code for POST request
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["title"] == payload["title"]
    assert response_json["body"] == payload["body"]
    # Fixed userid -> userId
    assert response_json["userId"] == payload["userId"]
    assert "id" in response_json

# Fixed remove class separator
@pytest.mark.nondestructive
def test_homepage_element_visibility(driver):
    driver.get("https://playwright.dev")
    # Fixed remove 3 parameter
    main_heading = driver.find_element(By.TAG_NAME, "h1")
    assert main_heading.is_displayed()