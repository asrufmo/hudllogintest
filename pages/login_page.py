from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # Login form locators
    USERNAME_INPUT = (By.ID, "username")
    CONTINUE_BTN = (By.NAME, "action")
    PASSWORD_INPUT = (By.ID, "password")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

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

    def is_login_page_loaded(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))
            return True
        except:
            return False

    def wait_until_loaded(self):
        self.wait.until(EC.presence_of_element_located(self.USERNAME_INPUT))

    def wait_until_login_page_is_ready(self):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT))