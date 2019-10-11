'''
@author: Quyen Doan
https://github.com/qdoan1651/OrangeHRM/tests_pytest/test_login_logout.py
'''
import os, pytest, sys
from selenium import webdriver

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_path)
from pages.login_page import LoginPage
from pages.home_page import HomePage 

@pytest.fixture()
def test_setup():
    global driver
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    chrome_path = os.path.join(project_path, 'drivers/chromedriver.v.77.exe')
    driver = webdriver.Chrome(chrome_path)
    driver.set_window_size(1600, 900)
    yield
    driver.close()
    driver.quit()

def test_login(test_setup):
    # login
    login_page = LoginPage(driver)
    login_page.login_as_admin()

def test_logout(test_setup):
    # login
    login_page = LoginPage(driver)
    login_page.login_as_admin()

    # log out
    home_page = HomePage(driver)
    home_page.logout()
