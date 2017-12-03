# coding=utf-8
import unittest

import time
from selenium import webdriver
class MemberManageTest(unittest.TestCase):
    def setUp(self):
        #变量前面加上self，表示这个变量是类的属性，可以被所有的方法访问
        #打开浏览器
        #driver声明在setUp方法之内，不能被其他方法访问
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
    def tearDown(self):
        #quit （）退出整个浏览器
        #close（）关闭一个浏览器标签
        #代码编写和调试的时候需要在quit（）方法前加一个时间等待，方便看清楚执行过程
        #正式运行的时候去掉时间等待，为了提高程序执行速度
        time.sleep()
        self.driver.quit()
    def test_add_member(self):
        #self.driver.get("")
        driver = self.driver
        driver.get("http://localhost/")
        driver.find_element_by_id("").send_keys("sun1")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()
        driver.find_element_by_name("username").send_keys("李一")
        driver.find_element_by_name("mobile_phone").send_keys("13200000000")
        driver.find_element_by_css_selector("[value='0']").click()
        birthday = driver.find_element_by_id("birthday")
        driver.execute_script("argumens[0].removeAttribute('birthday'),birthday")
        birthday.clear()
        birthday.send_keys("2000-12-30")
        driver.find_element_by_name("email").send_keys("1315@qq.com")
        driver.find_element_by_name("qq").send_keys("13512233")
        driver.find_element_by_class_name("button_search").click()




