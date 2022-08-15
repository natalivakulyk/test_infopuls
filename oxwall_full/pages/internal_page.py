from pages.base_page import BasePage
from pages.locators import InternalPageLocators


class InternalPage(BasePage):
    @property
    def sign_in_menu(self):
        return self.find_element(InternalPageLocators.SIGN_IN_MENU)

    @property
    def sign_up_menu(self):
        return self.find_visible_element(InternalPageLocators.SIGN_UP_MENU)

    @property
    def user_menu(self):
        return self.find_clickable_element(InternalPageLocators.USER_ICON)

    @property
    def sigh_out_bt(self):
        return self.user_menu.find_element(*InternalPageLocators.SIGN_OUT)

    @property
    def main_menu(self):
        return self.find_element(InternalPageLocators.MAIN_MENU)

    @property
    def active_menu(self):
        return self.find_element(InternalPageLocators.ACTIVE_MENU)

    def sign_in_click(self):
        self.sign_in_menu.click()

    def logout(self):
        if self.is_element_present(InternalPageLocators.USER_MENU):
            self.action_chain.move_to_element(self.user_menu)
            self.action_chain.perform()
            self.sigh_out_bt.click()
