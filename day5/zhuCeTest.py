# coding=utf-8
#有了MyTestCase以后，再写测试用例，就不需要重新写setup和tesrdown方法了
import os

from selenium import webdriver

from day5.myTestCase import MyTestCase


class ZhuCeTest(MyTestCase):
    """注册模块测试用例"""
    #因为myTestCase
    def test_zhu_ce(self):
        """打开注册页面的测试用例"""
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        #driver.current_url
        actual = driver.title
        expected = "用户注册 - 道e坊商城 - Powered by Haidao"

        base_path = os.path.dirname(__file__)
        #print(base_path)
        path = base_path.replace('day5','report/image/')
        #print(path)
        driver.get_screenshot_as_file(path+"zhuce.png")
        self.assertEqual(actual,expected)
