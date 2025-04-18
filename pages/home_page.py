from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    LOGIN_SELECT_BTN = (By.CSS_SELECTOR, "[data-qa-id='login-select']")
    HUDL_LOGIN_BTN = (By.XPATH, "//span[text()='Hudl']")
    BOTTOM_LOGIN_LINK = (By.LINK_TEXT, "Login")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to(self, url):
        self.driver.get(url)

    def click_main_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_SELECT_BTN)).click()

    def click_hudl_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.HUDL_LOGIN_BTN)).click()

    def click_footer_login_link(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait.until(EC.element_to_be_clickable(self.BOTTOM_LOGIN_LINK)).click()
