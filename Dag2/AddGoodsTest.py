#1.登陆
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

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
brand.submit()

