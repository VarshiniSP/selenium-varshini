import time
import pytest
from selenium import webdriver
from pages.addproduct import AddProduct
from pages.loginpage import LoginPage
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
class TestA:
    def test_addproduct(self, setup):
        self.driver=setup
        self.driver.get("https://www.saucedemo.com/v1/")
        self.lp=LoginPage(self.driver)
        self.lp.login("standard_user","secret_sauce")
        time.sleep(10)
        self.addprod=AddProduct(self.driver)
        self.addprod.addproduct()
