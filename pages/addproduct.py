from selenium.webdriver.common.by import By
class AddProduct:
    bpack="Backpack"
    inven=".btn_primary.btn_inventory"
    tag_name="path"

    def __init__(self, driver):
        self.driver = driver

    def addproduct(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.bpack).click()

        self.driver.find_element(By.CSS_SELECTOR, self.inven).click()

        self.driver.find_element(By.TAG_NAME, self.tag_name).click()
