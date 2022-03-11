import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--headless', action='store_true', default=False, help='Headless mode'
    )


def get_options(request):
    options = Options()
    if request.config.getoption('--headless'):
        options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1280')
    return options


@pytest.fixture
def driver_init(request):
    options = get_options(request)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    request.cls.driver = driver
    yield
    driver.quit()
