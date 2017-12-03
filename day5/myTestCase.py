# coding=utf-8
import unittest

import time
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 浏览器的版本和driver的版本必须匹配，才能用窗口最大化
        # driver.maximize_window()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
