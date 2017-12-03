# coding=utf-8
#1.登陆
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://localhost/index.php?m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_name("userverify").submit()
#2.商品管理
driver.find_element_by_link_text("商品管理").click()
#3.添加商品
driver.find_element_by_link_text("添加商品").click()
#4.商品名称
#开发很喜欢在一个页面中嵌套多个页面
#其中”商品管理“和”添加商品“属于页面根节点的网页
#其中商品名称属于frame框架里的子页
#之前讲过窗口切换，用于不同网页之间的页面切换
driver.switch_to.frame("mainFrame")#切换到子框架
driver.find_element_by_name("name").send_keys("iphone x")
# 5.商品分类
driver.find_element_by_xpath("//*[@id='1']").click()
driver.find_element_by_css_selector("[id='2']").click()
driver.find_element_by_id("6").click()
driver.find_element_by_id("7").click()
#双击是特殊的元素操作，所有的特殊操作被封装到ActionChains中
#链表结束一定要以perform结尾
#可以用来执行一组操作，只要最后以perform结束就可以了
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()

#6.商品品牌
brand = driver.find_element_by_name("brand_id")
Select(brand).select_by_index(1)
#driver.find_element_by_name("brand_id").find_element_by_css_selector("[value='1']").click()
#7.提交
# driver.find_element_by_class_name("button_search").click()
#brand.submit()
#商品图册
#因为真正负责文件上传的页面元素是<input type="file"...
#所以我们可以直接操作这个控件
#这个控件可以直接输入图片的路径

driver.find_element_by_link_text("商品图册").click()
#有些页面控件是javascipt在页面加载之后生成的
#implicitily_wait是用来判断整个网页是否加载完毕
#有时页面加载完，但是javascipt
time.sleep(3)
# driver.find_element_by_css_selector("#filePicker label").click()
driver.find_element_by_name("file").send_keys("D:/tupian.png")

ac = ActionChains(driver)
for i in range(10):
    ac.send_keys(Keys.ARROW_RIGHT)
ac.perform()
#driver.execute_script("window.scrollTo(200,100)")      scroll是滚动的意思，200，100是像素
# 点击开始上传，同时用3个class定位
driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
# alert这个控件不是直接弹出来的，需要时间等待
time.sleep(3)
driver.switch_to.alert.accept()
driver.find_element_by_class_name("button_search").click()
#页面太长，点击不了下面的按钮，怎么操作滚动条
#range是区间的意思，默认从零开始到长度减一结束   range（10） 表示0-9   10个数