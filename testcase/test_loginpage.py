import pytest
from selenium import webdriver
from pages.loginpage import LoginPage
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
class TestLogin:
    def test_login(self,setup):
        self.driver=setup
        self.driver.get("https://www.saucedemo.com/v1/")
        self.lp=LoginPage(self.driver)
        self.lp.login("standard_user","secret_sauce")