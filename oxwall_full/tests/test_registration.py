import os.path

import allure

from pages.dashboard_page import DashboardPage
from pages.join_page import JoinPage
from pages.main_page import MainPage
# from conftest import PROJECT_PATH


@allure.title("Sign up test ")
@allure.feature("User Registration")
@allure.story("Positive sign up")
def test_create_new_user(driver, user_data):
    # TODO: implement Page Objects methods
    main_page = MainPage(driver)
    main_page.open_sign_up_page()
    join_page = JoinPage(driver)
    join_page.input_username_text(user_data.username)
    join_page.input_email_text(user_data.email)
    join_page.input_password_text(user_data.password)
    join_page.input_repeat_password_text(user_data.password)
    join_page.input_real_name(user_data.real_name)
    if user_data.gender is not None:
        join_page.select_gender(user_data.gender)
    if user_data.birthday is not None:
        join_page.select_birthday(day=str(user_data.birthday.day), month=str(user_data.birthday.month), year=str(user_data.birthday.year))
    join_page.select_look_for_option([1, 2])
    join_page.select_here_for_option([1, 4])
    join_page.input_music_text('Music1\nMusic2\nMusic3')
    join_page.input_favourite_book_text('Book1\nBook2\nBook3')
    # join_page.upload_user_photo(os.path.join(PROJECT_PATH, 'data', '111.png'))
    join_page.press_join_button()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.user_menu.text == user_data.real_name

