import pytest
from support.pages.demo_page import DemoPage

@pytest.fixture
def demo_page(driver):
    return DemoPage(driver)

@pytest.mark.nondestructive
def test_homepage_verification(demo_page):
    demo_page.load()
    assert demo_page.has_main_heading()
    assert demo_page.has_get_started_button()
    assert demo_page.main_heading().text == "Playwright enables reliable end-to-end testing for modern web apps."
    demo_page.wait_until_get_started_button_visible()
    assert demo_page.get_started_button().is_displayed()

@pytest.mark.nondestructive
def test_navigation_verification(demo_page):
    demo_page.load()
    demo_page.get_started_button().click()
    assert "docs" in demo_page.driver.current_url
    assert demo_page.has_get_started_button()