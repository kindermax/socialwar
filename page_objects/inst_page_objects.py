
from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException
)

from page_objects.basic_page import BasePage
from locators import LoginFormLocators, CommentModalLocators

from utils import get_elem, wait_for_elem_disappear


class CommentModalPage(BasePage):

    def click_login_btn(self):
        get_elem(self.driver, CommentModalLocators.LOGIN_BTN).click()

    def enter_comment(self, comment: str):
        try:
            get_elem(
                self.driver, CommentModalLocators.COMMENT_TEXT_AREA
            ).send_keys(comment)
        except StaleElementReferenceException:
            self.enter_comment(comment)

    def submit_comment(self):
        get_elem(self.driver, CommentModalLocators.POST_COMMENT_BUTTON).click()

    def could_not_post(self):
        e = get_elem(self.driver, CommentModalLocators.COULD_NOT_POST_TEXT)
        return bool(e)


class LoginFormPage(BasePage):

    def login(self, username: str, password: str):
        get_elem(
            self.driver, LoginFormLocators.USERNAME_INPUT
        ).send_keys(username)
        get_elem(
            self.driver, LoginFormLocators.PASSWORD_INPUT
        ).send_keys(password)
        get_elem(self.driver, LoginFormLocators.SUBMIT_BTN).click()
        try:
            wait_for_elem_disappear(self.driver, LoginFormLocators.SUBMIT_BTN)
        except TimeoutException:
            raise Exception(
                'The error is occurred during the login with next '
                f'credentials:\nLogin: {username}; Password: {password}'
            )

    def skip_save_creds_in_browser(self):
        get_elem(self.driver, LoginFormLocators.SAVE_LOGIN_DATA_BTN).click()

    def allow_cookies(self):
        get_elem(self.driver, LoginFormLocators.ALLOW_COOKIES_DATA_BTN).click()
