from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import CommonPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # self.driver.implicitly_wait(2)
        self.wait = WebDriverWait(self.driver, 3, poll_frequency=0.1)
        self.action_chain = webdriver.ActionChains(self.driver)

    @property
    def message(self):
        return self.find_visible_element(CommonPageLocators.MESSAGE)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def find_element(self, locator):
        el = self.wait.until(EC.presence_of_element_located(locator),
                             message=f"No element with locator='{locator}'")
        return el

    def find_elements(self, locator):
        el = self.wait.until(EC.presence_of_all_elements_located(locator),
                             message=f"No element with locator='{locator}'")
        return el

    def find_visible_element(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator),
                             message=f"No visible element with locator='{locator}'")
        return el

    def find_clickable_element(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator),
                             message=f"No clickable element with locator='{locator}'")
        return el
