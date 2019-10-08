'''
@author: Raghav Pal
https://www.youtube.com/watch?v=BURK7wMcCwU&t=1538s
Selenium Python Small Sample Project | Page Object Model POM
Implement Page Object Model [20:00]
'''
import unittest, time, os
from selenium import webdriver
from tutorial.pages.login_page import LoginPage2
from tutorial.pages.home_page import HomePage2

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
        chrome_path = os.path.join(project_path, 'drivers/chromedriver.v.77.exe')
        cls.driver = webdriver.Chrome(chrome_path)
        cls.driver.set_window_size(1600, 1000)
        
    def test_admin_login(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com')
        
        # login
        login_page = LoginPage2(self.driver)
        login_page.enter_username('Admin')
        login_page.enter_password('admin123')
        login_page.click_login()

        # log out
        home_page = HomePage2(self.driver)
        home_page.click_welcome()
        time.sleep(1)
        home_page.click_logout()
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed.')

if __name__ == '__main__':
    unittest.main()

