'''
@author: Raghav Pal
https://www.youtube.com/watch?v=BURK7wMcCwU&t=1538s
Selenium Python Small Sample Project | Page Object Model POM
Implement unit test [12:40]
'''
from selenium import webdriver
import unittest, time, os

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
        self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        self.driver.find_element_by_id('btnLogin').click()
        
        # log out
        self.driver.find_element_by_id('welcome').click()
        time.sleep(1)
        self.driver.find_element_by_link_text('Logout').click()
        
        time.sleep(3)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test completed.')

if __name__ == '__main__':
    unittest.main()

