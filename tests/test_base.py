
import pytest

from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures('driver_init')
class TestBase(object):
    driver: WebDriver

    def open_page(self, url: str):
        self.driver.get(url)
