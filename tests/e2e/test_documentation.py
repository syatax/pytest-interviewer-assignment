import pytest
from support.pages.demo_page import DemoPage

@pytest.fixture
def demo_page(driver):
    return DemoPage(driver)

@pytest.mark.nondestructive
def test_homepage_verification(demo_page):
    demo_page.load()
    assert "Playwright" in demo_page.get_main_heading_text()
    demo_page.click_get_started()
    assert "docs" in demo_page.driver.current_url

@pytest.mark.nondestructive
def test_navigation_verification(demo_page):
    demo_page.load()
    demo_page.click_get_started()
    assert "docs" in demo_page.driver.current_url
    assert demo_page.has_navigation_menu()