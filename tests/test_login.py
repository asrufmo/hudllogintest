import pytest
from pages.login_page import LoginPage
from config import HUDL_USERNAME, HUDL_PASSWORD


@pytest.mark.positive
def test_login_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login(HUDL_USERNAME, HUDL_PASSWORD)

    assert "hudl.com/home" in driver.current_url or "dashboard" in driver.title.lower()


@pytest.mark.negative
def test_login_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login("invalid@example.com", HUDL_PASSWORD)

    assert "login" in driver.current_url.lower()  # Should not redirect to home


@pytest.mark.negative
def test_login_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.login(HUDL_USERNAME, "wrongpassword123")

    assert "login" in driver.current_url.lower()  # Still on login page


@pytest.mark.negative
def test_login_empty_password(driver):
    login_page = LoginPage(driver)
    login_page.go_to_login_page()
    login_page.enter_username(HUDL_USERNAME)
    login_page.click_continue()
    login_page.enter_password("")  # Leave password empty
    login_page.click_continue()

    assert "login" in driver.current_url.lower()
