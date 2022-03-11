from selenium.common.exceptions import (
    TimeoutException
)
from page_objects.basic_page import BasePage
from locators import (
    OKFormLocators,
)

from utils import get_elem, wait_for_elem_disappear


class LoginFormPage(BasePage):

    def login(self, username: str, password: str):
        get_elem(
            self.driver, OKFormLocators.LOGIN_INPUT
        ).send_keys(username)
        get_elem(
            self.driver, OKFormLocators.PASSWORD_INPUT
        ).send_keys(password)
        get_elem(self.driver, OKFormLocators.SUBMIT_BTN).click()
        try:
            wait_for_elem_disappear(self.driver, OKFormLocators.SUBMIT_BTN)
        except TimeoutException:
            raise Exception(
                'The error is occurred during the login with next '
                f'credentials:\nLogin: {username}; Password: {password}'
            )
