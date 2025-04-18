from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HudlLoginSelectorPage:
    # Locators
    HUDL_ICON = (By.XPATH, "//*[@id='logins_product-icon_hudl']/img")
    WYSCOUT_ICON = (By.XPATH, "//*[@id='logins_product-icon_wyscout']/img")
    WIMU_CLOUD_ICON = (By.XPATH, "//*[@id='logins_product-icon_volleymetrics']/img")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_hudl_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.HUDL_ICON)).click()
        print("Clicked Hudl icon")

    def click_wyscout_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.WYSCOUT_ICON)).click()

    def click_wimu_cloud_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.WIMU_CLOUD_ICON)).click()
