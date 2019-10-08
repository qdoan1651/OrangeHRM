'''
@author: Quyen Doan
https://github.com/qdoan1651/OrangeHRM/pages/base_page.py
- Base class for all pages
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        
    def go_to(self, url):
        self.driver.get(url)
        
    def get_page_url(self):
        return self.driver.current_url
    
    def get_page_title(self):
        return self.driver.title
    
    # Scrolling
    def scroll_element_into_view(self, by_loc):
        ele = self.driver.find_element(*by_loc)
        self.driver.execute_script("return arguments[0].scrollIntoView();", ele)

    def scroll_to_page_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
    def scroll_to_top_of_page(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
    
    # Implicit wait
    def set_implicit_wait(self, sec):
        """ Set the implicit wait with provided amount of time """
        self.driver.implicitly_wait(sec)
    
    # Explicit waits
    def wait_for_visibility_of_element(self, by_loc):
        """ An expectation for checking that an element is present on the DOM of a
        page and visible. Visibility means that the element is not only displayed
        but also has a height and width that is greater than 0.
        locator - used to find the element
        returns the WebElement once it is located and visible
        """
        return self.wait.until(EC.visibility_of_element_located(by_loc))
    
    def wait_for_invisibility_of_element(self, by_loc):
        """ An expectation for checking that an element is either invisible or not
        present on the DOM.
        locator - used to find the element
        """
        return self.wait.until(EC.invisibility_of_element_located(by_loc))
    
    def wait_for_clickability_of_element(self, by_loc):
        """ An Expectation for checking an element is visible and enabled such that
        you can click it.
        """
        return self.wait.until(EC.element_to_be_clickable(by_loc))
    
    def wait_for_present_of_element(self, by_loc):
        """ An expectation for checking that an element is present on the DOM
        of a page. This does not necessarily mean that the element is visible.
        locator - used to find the element
        returns the WebElement once it is located
        """
        return self.wait.until(EC.presence_of_element_located(by_loc))
    
    def wait_for_present_of_elements(self, by_loc):
        """ An expectation for checking that there is at least one element present
            on a web page.
            locator is used to find the element
            returns the list of WebElements once they are located
        """
        return self.wait.until(EC.presence_of_all_elements_located(by_loc))
    
    
if __name__ == '__main__':
    driver = webdriver.Chrome('D:/Workspace/Tools/drivers/chromedriver.v.77.exe')
    driver.set_window_size(1600, 900)
    
    base_page = BasePage(driver)
    base_page.go_to('https://amazon.com')
    print(base_page.get_page_title())
    print(base_page.get_page_url())