'''
@author: Quyen Doan
https://github.com/qdoan1651/OrangeHRM/locators/locators.py
'''
class Locators:
    # login page objects
    username_textbox_id = 'txtUsername'
    password_textbox_id = 'txtPassword'
    login_button_id = 'btnLogin'
    
    # home page objects
    welcome_link_id = 'welcome'
    logout_link_linktext = 'Logout'
    logout_link_xpath = '//div[@id="welcome-menu"]/ul/li[2]/a'

    admin_tab_id = 'menu_admin_viewAdminModule'
    user_management_tab_id = 'menu_admin_UserManagement'
    
    pim_tab_id = 'menu_pim_viewPimModule'
    employee_list_tab_id = 'menu_pim_viewEmployeeList'
    
    leave_tab_id = 'menu_leave_viewLeaveModule'
    leave_list_tab_id = 'menu_leave_viewLeaveList'
    
    time_tab_id = 'menu_time_viewTimeModule'
    define_time_sheet_id = 'defineTimesheet'
    
    recruitment_tab_id = 'menu_recruitment_viewRecruitmentModule'
    candidates_tab_id = 'menu_recruitment_viewCandidates'