import json
import time
import os.path

import pytest
from selenium import webdriver

from db.db_connector import OxwallDB
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from value_objects.users import User


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json", help="project config file name")
    # parser.addoption("--browser", action="store", default="Chrome", help="driver")


@pytest.fixture(scope="session")
def config(request):
    filename = request.config.getoption("--config")
    with open(os.path.join(PROJECT_DIR, filename), encoding="utf-8") as f:
        config = json.load(f)
    return config


@pytest.fixture()
def driver(selenium):
    driver = selenium
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def db(config):
    db = OxwallDB(**config["db"])
    yield db
    db.connection.close()


@pytest.fixture()
def open_oxwall_site(driver, base_url):
    driver.get(base_url)
    # driver.get(config["base_url"])
    # driver.get("https://demo.oxwall.com/")
    # driver.get("https://demos.softaculous.com/Oxwall")
    # driver.get("https://www.softaculous.com/softaculous/demos/Oxwall")

    # frame = driver.find_element(By.XPATH, "//iframe[2]")
    # driver.switch_to.frame(frame)
    return


@pytest.fixture()
def logged_user(driver, config):
    user = User(**config["admin"])
    main_page = MainPage(driver)
    main_page.sign_in_click()
    sign_in_page = SignInPage(driver)
    sign_in_page.login(user)
    time.sleep(5)
    yield user
    main_page.logout()


with open(os.path.join(PROJECT_DIR, "data", "user.json"), encoding="utf-8") as f:
    user_data = json.load(f)


@pytest.fixture(params=user_data, ids=[str(u) for u in user_data])
def user(request, db):
    u = User(**request.param)
    if u.username != "admin":
        db.create_user(u)
    yield u
    if u.username != "admin":
        db.delete_user(u)
