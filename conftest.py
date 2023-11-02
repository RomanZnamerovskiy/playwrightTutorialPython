import os

import pytest
from playwright.sync_api import Playwright
from pages.login_page_elements import LoginPage


@pytest.fixture()
def set_up(page):

    # browser = (playwright.chromium.launch(headless=False))
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()
    # login_page = LoginPage(page)
    page.goto("https://www.saucedemo.com/")
    page.set_default_timeout(1000)
    # login_page.login("standard_user", "secret_sauce")

    yield page


# @pytest.fixture(scope="session")
# def set_up(browser):
#
#     # browser = (playwright.chromium.launch(headless=False))
#     context = browser.new_context()
#     # Open new page
#     page = context.new_page()
#     # login_page = LoginPage(page)
#     page.goto("https://www.saucedemo.com/")
#     page.set_default_timeout(3000)
#     # login_page.login("standard_user", "secret_sauce")
#
#     yield page
#     # page.close()


@pytest.fixture()
def login_set_up(set_up):

    # browser = (playwright.chromium.launch(headless=False))
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()
    page = set_up
    login_page = LoginPage(page)
    # login_page.navigate()
    # page.set_default_timeout(3000)
    login_page.login("standard_user", "secret_sauce")

    yield page