# coding=utf-8
import unittest
from selenium import webdriver

class DengLuTest(unittest.TestCase):
    """登陆模块测试用例"""
    def setUp(self):
        #打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        #浏览器的版本和driver的版本必须匹配，才能用窗口最大化
        #driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
    def test_denglu(self):
        """登陆测试正常情况测试用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element_by_id("username").send_keys("sun1")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_class_name("login_btn ").click()
        print("当前用户名：sun1")