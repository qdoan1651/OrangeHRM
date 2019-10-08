'''
@author: Raghav Pal
https://www.youtube.com/watch?v=BURK7wMcCwU&t=1538s
Selenium Python Small Sample Project | Page Object Model POM
Create separate class for locators [36:15]
'''
class Locators():
    # login page objects
    username_textbox_id = 'txtUsername'
    password_textbox_id = 'txtPassword'
    login_button_id = 'btnLogin'
    
    # home page objects
    welcome_link_id = 'welcome'
    logout_link_linktext = 'Logout'
    logout_link_xpath = '//div[@id="welcome-menu"]/ul/li[2]/a'

