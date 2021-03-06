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

@pytest.fixture()
def test_setup():
    global driver
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    chrome_path = os.path.join(project_path, 'drivers/chromedriver.v.80.exe')
    driver = webdriver.Chrome(chrome_path)
    driver.set_window_size(1600, 900)
    login_page = LoginPage(driver)
    login_page.login_as_admin()
    yield
    driver.close()
    driver.quit()

def test_click_admin_tab(test_setup):
    homepage = HomePage(driver)
    homepage.click_admin_tab()
    assert homepage.get_management_tab_text() == 'User Management'
    
def test_click_pim_tab(test_setup):
    homepage = HomePage(driver)
    homepage.click_pim_tab()
    assert homepage.get_employee_list_tab_text() == 'Employee List'
 
def test_click_leave_tab(test_setup):
    homepage = HomePage(driver)
    homepage.click_leave_tab()
    assert homepage.get_leave_list_tab_text() == 'Leave List'
 
def test_click_time_tab(test_setup):
    homepage = HomePage(driver)
    homepage.click_time_tab()
    assert homepage.get_timesheets_tab_text() == 'Timesheets'
 
def test_click_recruitment_tab(test_setup):
    homepage = HomePage(driver)
    homepage.click_recruitment_tab()
    assert homepage.get_candidates_tab_text() == 'Candidates'

