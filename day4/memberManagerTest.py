# coding=utf-8
import unittest
#1.导入ddt代码库
import ddt

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from day4.readCsv2 import read


#2.装饰类
@ddt.ddt
class MemberManageTest(unittest.TestCase):
    #3.调用之前写好的read（）方法，获取配置文件中的数据
    member_info = read("member_info.csv")


    #在当前类只执行一次
    @classmethod
    def setUpClass(cls):
        print("所有方法之前，执行一次")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        #cls.driver.maximize_window
    @classmethod
    def tearDownClass(cls):
        time.sleep(20)
        cls.driver.quit()

    def test_a_log_in(self):
        print("登陆测试")
        driver = self.driver
        self.driver.get("http://localhost/admin.php")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password")\
            .send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()
    #python中集合前面的星号表示，表示把集合中的所有元素拆开，一个一个写
        #list =[”小红“，”小明“]
        #*list = ”小红“，”小明“
        #星号的作用就是把一个列表拆成2个str
        #加入一个方法需要接受2个参数，那么肯定不能传一个list进去
        #如果list中正好也有22个元素，这时在列表前面加一个星号
        #这时就不认为这时一个列表，而是2个参数了
    @ddt.data(*member_info)
    def testb_add_member(self,row):
        #每组测试数据就是一组测试用例，每条测试用例是独立的，所以这里不推荐用for循环
        #应该用ddt装饰器，去修饰方法，然后达到每条测试用例独立执行的目的
        #ddt 是数据驱动测试  data driver test
        #for row in read("member_info.csv"):
            #print("添加会员")
        driver = self.driver
        driver.find_element_by_link_text("会员管理").click()
        driver.find_element_by_link_text("添加会员").click()

        iframe_html = driver.find_element_by_css_selector("#mainFrame")
        driver.switch_to.frame(iframe_html)
        driver.find_element_by_name("username").send_keys(row[0])
        driver.find_element_by_name("mobile_phone").send_keys(row[1])
        driver.find_element_by_css_selector("[value='"+row[2]+"']").click()
        driver.find_element_by_id("birthday").send_keys(row[3])
        driver.find_element_by_name("email").send_keys(row[4])
        driver.find_element_by_name("qq").send_keys(row[5])
        driver.find_element_by_class_name("button_search").click()
        #切换到父框架
        #driver.switch_to.parent_frame()
        #切换到网页的根节点

        actual = driver.find_element_by_css_selector("#datagrid-row-r1-2-0 > td:nth-child(1) > div").test
        #expected 期望结果，来自于手动测试用例，需求文档
        expected = row[0]
        #断言类似于if  else语句
        #if actual == expected:
         #   print("测试通过")
        #else:
          #  print("测试失败")
        #断言是框架提供的，要想调用断言，那么必须加上self

        driver.switch_to.default_content()
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
