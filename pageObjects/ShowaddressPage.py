from pageObjects.Addaddress_Page import Addaddress_Page

class ShowaddressPage:
    def __init__(self, driver):
        self.driver = driver
    
    def add_address(self):
        self.driver.find_element_by_css_selector("[data-test='create']").click()
        add_address_page = Addaddress_Page(self.driver)
        return add_address_page
    
    
    def title(self):
        title = self.driver.find_element_by_css_selector(".container h2").text
        return title
        
        