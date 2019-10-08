'''
@author: Quyen Doan
https://github.com/qdoan1651/OrangeHRM/tests/test_base_page.py
- Tests for BasePage class
'''
import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

def test_scrolling():
    # scroll to 'Privacy Notice' at bottom of page
    print('Scrolling to "Privacy Notice" at bottom of page...')
    loc = (By.XPATH, '//a[text()="Privacy Notice"]')
    base_page.scroll_element_into_view(loc)
    time.sleep(3)
    
    # scroll to top of page
    print('Scrolling to top of page...')
    base_page.scroll_to_top_of_page()
    time.sleep(3)
    
    # now scroll to bottom of page
    print('Scrolling to bottom of page...')
    base_page.scroll_to_page_bottom()
    

if __name__ == '__main__':
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    chrome_path = os.path.join(project_path, 'drivers/chromedriver.v.77.exe')
    driver = webdriver.Chrome(chrome_path)
    driver.set_window_size(1600, 900)
    
    base_page = BasePage(driver)
    base_page.go_to('https://amazon.com')
    print(base_page.get_page_title())
    print(base_page.get_page_url())
    
    # click on Best Sellers tab
#     loc = (By.XPATH, '//a[text()="Best Sellers"]')
#     base_page.wait_for_visibility_of_element(loc).click()
    
    test_scrolling()