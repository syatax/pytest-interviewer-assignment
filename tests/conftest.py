import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tempfile

APP_HOST = "https://playwright.dev"
DEFAULT_WAIT = 10

def pytest_addoption(parser):
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run browser in headless mode"
    )

@pytest.fixture(scope="session")
def chrome_options(request):
    opts = Options()
    if request.config.getoption("--headless"):
        opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    return opts

@pytest.fixture(scope="function")
def driver(chrome_options):
    profile_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={profile_dir}")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(DEFAULT_WAIT)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def base_url():
    return APP_HOST
