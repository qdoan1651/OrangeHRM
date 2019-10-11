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
        
        self.admin_tab_loc = (By.ID, Locators.admin_tab_id)
        self.user_management_tab_loc = (By.ID, Locators.user_management_tab_id)
        
        self.pim_tab_loc = (By.ID, Locators.pim_tab_id)
        self.employee_list_tab_loc = (By.ID, Locators.employee_list_tab_id)
        
        self.leave_tab_loc = (By.ID, Locators.leave_tab_id) 
        self.leave_list_tab_loc = (By.ID, Locators.leave_list_tab_id)
        
        self.time_tab_loc = (By.ID, Locators.time_tab_id)
        self.define_timesheet_period_loc = (By.ID, Locators.define_time_sheet_id)
        
        self.recruitment_tab_loc = (By.ID, Locators.recruitment_tab_id)
        self.candidates_tab_loc = (By.ID, Locators.candidates_tab_id)
        
    def click_welcome(self):
        super().wait_for_visibility_of_element(self.welcome_link).click()
        
    def click_lougout(self):
        super().wait_for_visibility_of_element(self.logout_link).click()
        
    def logout(self):
        self.click_welcome()
        self.click_lougout()
        
    def click_admin_tab(self):
        super().wait_for_visibility_of_element(self.admin_tab_loc).click()
        ele = super().wait_for_visibility_of_element(self.user_management_tab_loc)
        assert ele.text == 'User Management'
        
    def click_pim_tab(self):
        super().wait_for_visibility_of_element(self.pim_tab_loc).click()
        ele = super().wait_for_visibility_of_element(self.employee_list_tab_loc)
        assert ele.text == 'Employee List'
        
    def click_leave_tab(self):
        super().wait_for_visibility_of_element(self.leave_tab_loc).click()
        ele = super().wait_for_visibility_of_element(self.leave_list_tab_loc)
        assert ele.text == 'Leave List'

    def click_time_tab(self):
        super().wait_for_visibility_of_element(self.time_tab_loc).click()
        ele = super().wait_for_visibility_of_element(self.define_timesheet_period_loc)
        assert ele.text == 'Define Timesheet Period'
        
    def click_recruitment_tab(self):
        super().wait_for_visibility_of_element(self.recruitment_tab_loc).click()
        ele = super().wait_for_visibility_of_element(self.candidates_tab_loc)
        assert ele.text == 'Candidates'