import json
import time
import os.path

import allure
import pytest

from pages.dashboard_page import DashboardPage
from data.random_string import random_string
from conftest import PROJECT_DIR

with open(os.path.join(PROJECT_DIR, "data", "posts_text.json"), encoding="utf8") as f:
    posts_text = json.load(f)

posts_text.append(random_string(minlen=3, maxlen=30, enter=True, cyrillic=True))

posts_text[0] = pytest.param(posts_text[0], marks=pytest.mark.smoke)


@allure.title("Post create test")
@allure.feature("Post")
@allure.story("Create text post (without photos)")
@pytest.mark.parametrize("input_text", posts_text)
def test_create_post(driver, open_oxwall_site, logged_user, input_text, db):
    dashboard_page = DashboardPage(driver)
    initial_amount_of_posts = dashboard_page.calculate_posts()
    dashboard_page.input_text_of_new_post(input_text)
    dashboard_page.submit_post()
    dashboard_page.wait_new_post_appear(initial_amount_of_posts)
    with allure.step(f'THEN this post block has this {input_text} and author as this user and time "within 1 minute"'):
        posts = dashboard_page.posts
        new_post = posts[0]
        assert db.get_last_text_post() == input_text
        assert new_post.text == input_text
        assert new_post.user == logged_user.username.title()


@allure.title("Add like test")
@allure.feature("Post")
@allure.story("Add like to middle post")
def test_add_like_to_middle_post(driver, open_oxwall_site, logged_user):
    dashboard_page = DashboardPage(driver)
    posts = dashboard_page.posts
    middle_post = posts[len(posts)//2]
    middle_post.add_like()
    time.sleep(0.5)
    assert middle_post.like_counter.text == "1"


@allure.title("Empty post create test")
@allure.feature("Post")
@allure.story("Try to create empty post ")
def test_submit_post_without_text(driver, open_oxwall_site, logged_user):
    dashboard_page = DashboardPage(driver)
    initial_amount_of_posts = dashboard_page.calculate_posts()
    dashboard_page.post_text_field.click()
    dashboard_page.submit_post()
    assert dashboard_page.message.text == "PLEASE FILL THE FORM PROPERLY"
    posts = dashboard_page.calculate_posts()
    assert initial_amount_of_posts == posts
