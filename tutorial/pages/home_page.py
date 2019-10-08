'''
@author: Raghav Pal
https://www.youtube.com/watch?v=BURK7wMcCwU&t=1538s
Selenium Python Small Sample Project | Page Object Model POM
Implement Page Object Model [20:00]
'''
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = 'welcome'
        self.logout_link_linktext = 'Logout'
        
    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()
        
    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linktext).click()

'''
@author: Raghav Pal
https://www.youtube.com/watch?v=BURK7wMcCwU&t=1538s
Selenium Python Small Sample Project | Page Object Model POM
Create separate class for locators [36:15]
'''
from tutorial.locators.locators import Locators
class HomePage2:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = Locators.welcome_link_id
#         self.logout_link_linktext = Locators.logout_link_linktext
        self.logout_link_xpath = Locators.logout_link_xpath
        
    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()
        
    def click_logout(self):
#         self.driver.find_element_by_link_text(self.logout_link_linktext).click()   
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()   
                    