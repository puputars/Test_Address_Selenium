class ResultaddressPage():
    def __init__(self, driver):
        self.driver = driver
        
    def result_address(self, id_address):
        return self.driver.find_element_by_css_selector("[data-test='show-{}']".format(id_address)).click()
    
    
    def screenshot(self, id_address):
        return self.driver.save_screenshot("{}.png".format(id_address))
        