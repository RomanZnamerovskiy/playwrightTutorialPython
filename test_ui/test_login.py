import os

from playwright.sync_api import Playwright, sync_playwright, expect

# import utils.secret_config
from pages.login_page_elements import LoginPage
import pytest


try:
    PASSWORD = os.environ['PASSWORD']
except KeyError:
    import utils.secret_config
    PASSWORD = utils.secret_config.PASSWORD


# @pytest.mark.parametrize("username, password", [("standard_user",  "secret_sauce"),
#                                              pytest.param("fakeemail", "fakepassword", marks=pytest.mark.xfail),
#                                              pytest.param("standard_use", "secret_sauce", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("username", ["standard_user",
                                             pytest.param("fake_user", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", [PASSWORD,
                                             pytest.param("fake_password", marks=pytest.mark.xfail)])
@pytest.mark.regression
def test_login_with_different_users_and_passwords(set_up, username, password) -> None:
    page = set_up
    login_page = LoginPage(page)
    login_page.login(username, password)
    expect(login_page.login_button).to_be_hidden(timeout=1000)

    # ---------------------


# @pytest.mark.skip(reason="not ready")
@pytest.mark.smoke
@pytest.mark.xfail(reason="not ready")
def test_user_see_login_button(set_up) -> None:
    page = set_up

    login_page = LoginPage(page)
    expect(login_page.login_button).to_be_hidden()
    # expect(login_page.login_button).to_be_visible()

    # ---------------------


