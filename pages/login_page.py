from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL


class LoginPage:
    # Locators
    LOGIN_SELECT_BTN = (By.CSS_SELECTOR, "[data-qa-id='login-select']")
    HUDL_LOGIN_BTN = (By.XPATH, "//span[text()='Hudl']")
    USERNAME_INPUT = (By.ID, "username")
    CONTINUE_BTN = (By.NAME, "action")
    PASSWORD_INPUT = (By.ID, "password")

    # Locators for bottom login link
    BOTTOM_LOGIN_LINK = (By.LINK_TEXT, "Login")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_login_page(self):
        self.driver.get(BASE_URL)
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_SELECT_BTN)).click()
        self.wait.until(EC.element_to_be_clickable(self.HUDL_LOGIN_BTN)).click()

    def enter_username(self, username):
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT)).send_keys(username)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN)).click()

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT)).send_keys(password)

    def login(self, username, password):
        self.enter_username(username)
        self.click_continue()
        self.enter_password(password)
        self.click_continue()

    def click_bottom_login_link(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTTOM_LOGIN_LINK)).click()

    def is_login_page_loaded(self):
        return "Login" in self.driver.title
