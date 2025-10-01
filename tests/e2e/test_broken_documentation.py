import pytest
from support.pages.demo_page import DemoPage

#
# E2E Test Implementation - Documentation Homepage
# 
# Implement ONE comprehensive test that verifies the core functionality
# of the Playwright documentation homepage (https://playwright.dev).
# 
# Focus on demonstrating your testing strategy and technical approach
# rather than covering every possible scenario.
#

@pytest.fixture
def demo_page(driver):
    return DemoPage(driver)

@pytest.mark.nondestructive
def test_homepage_verification(demo_page):
    #
    # TASK: Implement a comprehensive test for the Playwright homepage
    # 
    # Your test should verify:
    # 1. Page loads correctly with expected content
    # 2. Primary user action works (Get Started button)
    # 3. Navigation to documentation functions properly
    # 4. Navigate to Best Practices page with anchor link
    # 5. Verify specific code examples are present in documentation
    # 
    # EVALUATION FOCUS:
    # - How do you structure your test logic?
    # - What selectors do you choose and why?
    # - How do you handle waiting and timing?
    # - How do you validate complex page content?
    # - What assertions do you consider most important?
    # 
    # Use the DemoPage page object where appropriate.
    # Write this as if it were going into production.
    #
    
    # TODO: Implement comprehensive E2E test
    # 
    # Requirements:
    # 1. Navigate to https://playwright.dev and verify homepage
    # 2. Use page object methods to interact with elements
    # 3. Navigate to https://playwright.dev/docs/best-practices#use-locators
    # 4. Verify the code example exists: page.getByRole('button', { name: 'submit' });
    # 5. Implement proper waiting and error handling