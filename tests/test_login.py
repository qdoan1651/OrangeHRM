'''
@author: Quyen Doan
https://github.com/qdoan1651/OrangeHRM/tests/test_login.py
- Update modules import due to adding BasePage class as parent class
'''

import unittest, time, os
from selenium import webdriver
from HtmlTestRunner import HTMLTestRunner

from pages.login_page import LoginPage
from pages.home_page import HomePage

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        chrome_path = os.path.join(project_path, 'drivers/chromedriver.v.77.exe')
        cls.driver = webdriver.Chrome(chrome_path)
        cls.driver.set_window_size(1600, 1000)
        
    def test_admin_login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com')
        
        # login
        login_page = LoginPage(self.driver)
        login_page.login_as_admin()

        # log out
        home_page = HomePage(self.driver)
        home_page.logout()
        
        time.sleep(3)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed.')

if __name__ == '__main__':
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    reports_path = os.path.join(project_path, 'reports')
    unittest.main(testRunner=HTMLTestRunner(output=reports_path))


