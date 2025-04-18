import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from config import HUDL_USERNAME, HUDL_PASSWORD, BASE_URL


@pytest.mark.positive
def test_login_valid_credentials(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    home_page.go_to(BASE_URL)
    home_page.click_main_login()
    home_page.click_hudl_icon()

    login_page.login(HUDL_USERNAME, HUDL_PASSWORD)

    assert "hudl.com/home" in driver.current_url or "dashboard" in driver.title.lower()


@pytest.mark.negative
def test_login_invalid_username(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    home_page.go_to(BASE_URL)
    home_page.click_main_login()
    home_page.click_hudl_icon()

    login_page.login("invalid@example.com", HUDL_PASSWORD)

    assert "login" in driver.current_url.lower()


@pytest.mark.negative
def test_login_invalid_password(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    home_page.go_to(BASE_URL)
    home_page.click_main_login()
    home_page.click_hudl_icon()

    login_page.login(HUDL_USERNAME, "wrongpassword123")

    assert "login" in driver.current_url.lower()


@pytest.mark.negative
def test_login_empty_password(driver):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)

    home_page.go_to(BASE_URL)
    home_page.click_main_login()
    home_page.click_hudl_icon()

    login_page.enter_username(HUDL_USERNAME)
    login_page.click_continue()
    login_page.enter_password("")  # Leave password empty
    login_page.click_continue()

    assert "login" in driver.current_url.lower()