from selenium.webdriver.common.by import By


class LoginPage:
    txtbox_username_id = "user-name"
    txtbox_password_id = "password"
    button_login_CLASS_NAME = "btn_action"

    def __init__(self, driver):
        self.driver = driver

    def login(self, username,password):
        uname = self.driver.find_element(By.ID, self.txtbox_username_id)
        uname.send_keys(username)

        pwd = self.driver.find_element(By.ID, self.txtbox_password_id)
        pwd.send_keys(password)


        self.driver.find_element(By.CLASS_NAME, self.button_login_CLASS_NAME).click()
