from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import PostBlockLocators


class PostBlock:
    def __init__(self, element, driver):
        self.element = element
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3, poll_frequency=0.1)

    @property
    def user(self):
        return self.element.find_element(*PostBlockLocators.POST_USER).text

    @property
    def text(self):
        element = self.element.find_element(*PostBlockLocators.POST_TEXT)
        element = self.wait.until(EC.visibility_of(element))
        return element.text

    @property
    def time(self):
        return self.element.find_element(*PostBlockLocators.POST_TIME).text

    @property
    def like_bt(self):
        return self.element.find_element(*PostBlockLocators.LIKE)

    @property
    def like_counter(self):
        return self.element.find_element(*PostBlockLocators.LIKE_COUNTER)

    def add_like(self):
        self.like_bt.click()
