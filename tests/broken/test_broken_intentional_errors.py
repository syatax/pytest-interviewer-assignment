import pytest
from support.pages.demo_page import DemoPage
from selenium.webdriver.common.by import By

@pytest.fixture
def demo_page(driver):
    return DemoPage(driver)

#
# Test Suite - Debug and Fix Issues
# 
# This file contains several common testing errors.
# Your task is to identify and fix all issues to make the tests pass.
#

@pytest.mark.nondestructive
def test_homepage_verification(demo_page):
    demo_page.load()
    assert demo_page.has_main_heading()
    assert demo_page.has_get_started_button()
    assert demo_page.main_heading().text == "Playwright enables reliable end-to-end testing for modern web apps"
    demo_page.wait_until_get_started_button_visible()
    assert demo_page.get_started_button().is_displayed?()

@pytest.mark.nondestructive
def test_navigation_verification(demo_page):
    demo_page.load()
    demo_page.get_started_button().set()
    assert "docs" in demo_page.driver.current_title
    assert demo_page.has_get_started_button

@pytest.mark.nondestructive
def test_api_integrations():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "New Post",
        "body": "Content",
        "userId": 1
    }
    response = requests.get(url, json=payload)

    assert response.status_code == 200
    response_json = response.json()
    assert response_json["title"] == payload["title"]
    assert response_json["body"] == payload["body"]
    assert response_json["userid"] == payload["userId"]
    assert "id" in response_json

class StandaloneTest:
    @pytest.mark.nondestructive
    def test_homepage_element_visibility(driver):
        driver.get("https://playwright.dev")
        main_heading = driver.find_element(By.TAG_NAME, "h1", 'Main header')
        assert main_heading.is_displayed()