'''
@author: Quyen Doan
https://github.com/qdoan1651/OrangeHRM/pages/home_page.py
- Added BasePage class as parent class
'''
from selenium.webdriver.common.by import By
from locators.locators import Locators
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.welcome_link = (By.ID, Locators.welcome_link_id)
        self.logout_link = (By.XPATH, Locators.logout_link_xpath)
        
    def click_welcome(self):
        super().wait_for_visibility_of_element(self.welcome_link).click()
        
    def click_lougout(self):
        super().wait_for_visibility_of_element(self.logout_link).click()
        
    def logout(self):
        self.click_welcome()
        self.click_lougout()
