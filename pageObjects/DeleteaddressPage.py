import time

class DeleteaddressPage():
    def __init__(self, driver):
        self.driver = driver
        
    def delete_address(self, id_address):
        return self.driver.find_element_by_css_selector("[data-test='destroy-{}']".format(id_address)).click()
    
    
    def alert_delete(self):  
        alert = self.driver.switch_to.alert
        time.sleep(2)
        alert.accept()