'''
@author: Raghav Pal
https://www.youtube.com/watch?v=BURK7wMcCwU&t=1538s
Selenium Python Small Sample Project | Page Object Model POM
Implement Page Object Model [20:00]
'''
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_id = 'txtUsername'
        self.password_id = 'txtPassword'
        self.login_id = 'btnLogin'
        
    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)
        
    def click_login(self):
        self.driver.find_element_by_id(self.login_id).click()
        
'''
@author: Raghav Pal
https://www.youtube.com/watch?v=BURK7wMcCwU&t=1538s
Selenium Python Small Sample Project | Page Object Model POM
Create separate class for locators [36:15]
'''
from tutorial.locators.locators import Locators
class LoginPage2:
    def __init__(self, driver):
        self.driver = driver
        self.username_id = Locators.username_textbox_id
        self.password_id = Locators.password_textbox_id
        self.login_id = Locators.login_button_id
        
    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(password)
        
    def click_login(self):
        self.driver.find_element_by_id(self.login_id).click()
