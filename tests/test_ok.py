import itertools
import os
import random
import time
from datetime import datetime

import pytest
from selenium.webdriver import Keys

from locators import OKFormLocators
from tests.test_base import TestBase

from page_objects.ok_page_objects import (
    LoginFormPage,
)

from utils import (
    select_random_elem,
    get_elem,
)
from files.comment import (
    COMMENTS_OK_NEW,
)
from logger import get_logger


LOGGER = get_logger(__name__)


def move_user_cursor(user, failed=False):
    users_file = 'ok_users.txt'
    failed_file = 'ok_users_failed.txt'
    ok_file = 'ok_users_done.txt'

    done_file = ok_file
    if failed:
        done_file = failed_file

    with open(f'../files/ok_files/{done_file}', 'a') as f:
        f.write(user + '\n')

    with open(f'../files/ok_files/{users_file}', 'r') as f:
        users = f.readlines()
        users = set([u.strip() for u in users])

    with open(f'../files/ok_files/{users_file}', 'w') as f:
        try:
            users.remove(user)
        except KeyError:
            ...
        f.writelines([u + '\n' for u in users])

    LOGGER.info('Done with user %s', user)


# list of strings in format 'phone:password',
ACCOUNTS = [
]


def get_accounts():
    return [
        a.split(':') for a in ACCOUNTS
    ]


def get_users():
    users_file = 'ok_users.txt'
    with open(f'../files/ok_files/{users_file}', 'r') as f:
        users = f.readlines()
        users = set([u.strip() for u in users])
        return list(users)


def get_cookies():
    with open('../files/ok_files/ok_cookies.txt', 'r') as f:
        cookies = f.readlines()
        cookies = set([c.strip() for c in cookies])
        return list(cookies)


PHOTOS = os.listdir('../files/photo')


class TestOk(TestBase):
    def send_message(self, message: str):
        inp = get_elem(
            self.driver, OKFormLocators.MSG_INPUT
        )
        LOGGER.info('Sending text')
        inp.send_keys(message)
        LOGGER.info('Text sent')

        for count in range(1, 4):
            LOGGER.info('Uploading photo')
            self.upload_photo()
            LOGGER.info('Waiting for photo to upload')
            self.wait_element_count(count)
        LOGGER.info('Sending whole message')
        inp.send_keys(Keys.RETURN)
        LOGGER.info('Whole message sent')

    def upload_photo(self):
        upload_by, upload_loc = OKFormLocators.FILE_INPUT
        photo_file = random.choice(PHOTOS)
        photo_path = os.path.abspath('../files/photo/' + photo_file)
        self.driver.find_element(upload_by, upload_loc).send_keys(photo_path)

    def wait_element_count(self, wait_len):
        uploaded_by, uploaded_loc = OKFormLocators.UPLOADED_FILE
        for _ in range(30):
            uploaded = self.driver.find_elements(uploaded_by, uploaded_loc)
            if len(uploaded) == wait_len:
                time.sleep(0.5)
                return
            else:
                time.sleep(0.5)

    def login_by_cookie(self, cookie):
        self.driver.delete_all_cookies()
        self.driver.add_cookie({
            'httpOnly': True,
            "path": "/",
            "domain": ".ok.ru",
            "name": "AUTHCODE",
            'sameSite': 'None',
            'secure': True,
            "value": cookie
        })
        self.driver.refresh()

    def login_by_password(self, user):
        login_form = LoginFormPage(self.driver)
        login_form.login(user[0], user[1])

    @pytest.mark.ok
    @pytest.mark.parametrize('user', get_accounts())
    def test_generate_cookies(self, user):
        self.open_page('https://ok.ru/')
        try:
            self.login_by_password(user)
        except Exception:
            LOGGER.exception("Failed to get cookie for user %s", user)
            return
        cookie = self.driver.get_cookie('AUTHCODE')
        if not cookie:
            LOGGER.error("No cookie for user %s", user)
            return
        with open('../files/ok_files/ok_cookies.txt', 'a') as f:
            f.write(cookie['value'] + '\n')

    @pytest.mark.ok
    def test_send_message(self):
        start = datetime.now()
        cookies = get_cookies()
        random.shuffle(cookies)
        total_failed_count = 0

        # for user in get_accounts():
        #     self.login_by_password(user)
        for cookie in itertools.cycle(cookies):
            if (datetime.now() - start).seconds >= 60*30:
                LOGGER.info('Please generate new sessions')
                return
            if total_failed_count >= 10:
                LOGGER.info('Total failed count is large')
                return
            self.open_page('https://ok.ru/')
            self.login_by_cookie(cookie)

            print('Using cookie', cookie)
            failed_count = 0
            for u in get_users()[:3]:
                if failed_count >= 1:
                    LOGGER.error("Too much errors. Spam stopped")
                    break
                try:
                    self.open_page(f'https://ok.ru/messages/{u}')

                    comment = select_random_elem(COMMENTS_OK_NEW)
                    self.send_message(comment)
                    sleep_time = random.randint(4, 6)
                    time.sleep(sleep_time)
                    move_user_cursor(u)
                except Exception as e:
                    failed_count += 1
                    total_failed_count += 1
                    LOGGER.error("The message wasn't sent. %s" ,e)
                    move_user_cursor(u, True)
