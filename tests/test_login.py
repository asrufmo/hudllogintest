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


@pytest.mark.positive
def test_login_from_bottom_link(driver):
    login_page = LoginPage(driver)
    login_page.driver.get("https://www.hudl.com")  # Navigate directly to the homepage

    # Scroll to the bottom of the page
    login_page.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Click the login link at the bottom of the page
    login_page.click_bottom_login_link()

    # Verify that we are on the login page
    assert login_page.is_login_page_loaded(), "Login page did not load!"