from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.locators import SignInPageLocators


class SignInPage(BasePage):
    @property
    def username_field(self):
        return self.find_element(SignInPageLocators.USERNAME_FIELD)

    @property
    def password_field(self):
        element = self.find_element(SignInPageLocators.PASSWORD_FIELD)
        return element

    @property
    def sign_in_button(self):
        element = self.find_element(SignInPageLocators.SIGN_IN_BUTTON)
        return element

    def input_username(self, username):
        self.username_field.clear()
        self.username_field.send_keys(username)

    def input_password(self, password):
        self.password_field.clear()
        self.password_field.send_keys(password)

    def click_sign_in(self):
        self.sign_in_button.click()

    def submit(self):
        self.password_field.send_keys(Keys.ENTER)

    def login(self, user):
        self.input_username(user.username)
        self.input_password(user.password)
        self.sign_in_button.click()


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    signin_page = SignInPage(driver)
    signin_page.username_field.send_keys("sdfdfg")
    signin_page.password_field()
    # signin_page.login()

