'''
@author: Quyen Doan
https://github.com/qdoan1651/OrangeHRM/pages/login_page.py
- Added BasePage class as parent class
'''
from selenium.webdriver.common.by import By

from locators.locators import Locators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username = (By.ID, Locators.username_textbox_id)
        self.password = (By.ID, Locators.password_textbox_id)
        self.login = (By.ID, Locators.login_button_id)
        
    def enter_username(self, username):
        super().wait_for_visibility_of_element(self.username).clear()
        super().wait_for_visibility_of_element(self.username).send_keys(username)
        
    def enter_password(self, password):
        super().wait_for_visibility_of_element(self.password).clear()
        super().wait_for_visibility_of_element(self.password).send_keys(password)
        
    def click_login(self):
        super().wait_for_clickability_of_element(self.login).click()
        
    def login_as_admin(self, username='Admin', password='admin123'):
        self.driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
        
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        