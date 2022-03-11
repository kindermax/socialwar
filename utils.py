import random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC


def get_elem(driver, locator: tuple, timeout=15) -> WebElement:
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))


def get_elemets(driver,  locator: tuple) -> WebElement:
    return WebDriverWait(driver, 15).until(EC.visibility_of_any_elements_located(locator))


def wait_for_elem_disappear(driver, locator: tuple, timeout=15):
    return WebDriverWait(driver, timeout).until(EC.invisibility_of_element_located((locator)))


def select_random_elem(seq):
    return random.choice(seq)
