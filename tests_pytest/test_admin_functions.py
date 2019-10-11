'''
@author: Quyen Doan
https://github.com/qdoan1651/OrangeHRM/tests_pytest/test_admin_functions.py
'''
import os, pytest, sys
from selenium import webdriver

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_path)
from pages.login_page import LoginPage
from pages.home_page import HomePage 

class TestOrangeHRM():
    @pytest.fixture()
    def test_setup(self):
        global driver
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        chrome_path = os.path.join(project_path, 'drivers/chromedriver.v.77.exe')
        driver = webdriver.Chrome(chrome_path)
        driver.set_window_size(1600, 900)
        yield
        driver.close()
        driver.quit()
    
    def test_click_admin_tab(self, test_setup):
        # login
        login_page = LoginPage(driver)
        login_page.login_as_admin()
    
    def test_click_pim_tab(self, test_setup):
        # login
        login_page = LoginPage(driver)
        login_page.login_as_admin()
 
    def test_click_leave_tab(self, test_setup):
        # login
        login_page = LoginPage(driver)
        login_page.login_as_admin()
 
    def test_click_time_tab(self, test_setup):
        # login
        login_page = LoginPage(driver)
        login_page.login_as_admin()
 
    def test_click_recruitment_tab(self, test_setup):
        # login
        login_page = LoginPage(driver)
        login_page.login_as_admin()
 