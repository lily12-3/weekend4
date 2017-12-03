# coding=utf-8
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
    title = "用户登录 - 道e坊商城 - Powered by Haidao"
    url = "http://localhost/index.php?m=user&c=public&a=login"
    #小括号表示元祖，元祖中有2个元素，第一个元素是控件的定位方式
    #第二个元素，控件定位方式的具体值
    username_input_local = (By.ID,"username")
    password_input_local = (By.ID,"password")
    login_batton_local = (By.CLASS_NAME,"login_btn")

    def open(self):
        self.driver.get(self.url)

    def input_username(self, username):
        """fgtdfg"""
        #self.driver.find_element_by_id("username").send_keys(username)
        #self.driver.find_element(By.ID,"username").send_keys(username)
        self.driver.find_element(*self.username_input_local).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(*self.password_input_local).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_batton_local).click()
