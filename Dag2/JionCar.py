import time
from selenium import webdriver
#firefox浏览器 15版本以下的不需要驱动文件，46开始firefox浏览器，也需要把driver.exe文件放到环境变量
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
#隐式等待，一经设置，对后面的语句都有效果，所以在创建浏览器时设置一次就可以了
#implicitly 含蓄的，委婉
driver.implicitly_wait(30)
driver.get("http://localhost/")
#在点击登陆按钮之前，我们需要先删除target属性
#但是javascript定位方式比selenium麻烦
#可以用selenium的定位方式来替换javascript的定位方式
#用argument关键字，把元素定位作为一个参数，替换到javascript语句中
login_link = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')",login_link)#arguments[0]后面的第一个参数，也可以接多个参数
login_link.click()
driver.find_element_by_id("username").send_keys("sun1")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("password").submit()
time.sleep(5)
#Alt+enter  可以自动寻包
#time.sleep到底设成几秒，几秒都不好
#应该是用户隐式等待，会自动判断网页是否加载完毕，当加载完毕立刻开始后续的操作
#我们需要设一个最大是时间，不能让程序无限等待，一般这个时间是30秒
driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()

iphone_link = "div.shop_01-imgbox > a"#2个class
#img 是标签名，>标签前面的是父节点，后面的子节点
#如果想在css中写class属性，那么前面需要加上小数点
#:nth-child(2),表示当前节点在家排行老二，其父亲的第二个儿子
#为什么我们要把css selector中的内容改的越短越好，涉及到越多的节点，那么代码的健壮性和可维护性就越差，
#因为开发一旦修改页面时，修改了这些节点，那么元素就会定位失败
iphone = driver.find_element_by_css_selector(iphone_link)
driver.execute_script("arguments[0].removeAttribute('target')",iphone)
iphone.click()
#点击加入购物车按钮
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()
#点击添加新地址
driver.find_element_by_class_name("add-address").click()
driver.find_element_by_name("address[address_name]").send_keys("联想")
driver.find_element_by_name("address[mobile]").send_keys("13212345678")
#下拉框是一种比较特殊的网页元素，selenium专门为下拉框提供了一种定位方式
#需要把这个元素从webElement类型转换成select类型
#select 这个类中封装了很多操作下拉框的方法
sheng = driver.find_element_by_id("add-new-area-select")
Select(sheng).select_by_value('230000')
#定位第二个下拉框
shi = driver.find_elements_by_tag_name("select")[1]
Select(shi).select_by_index(2)
qu = driver.find_elements_by_tag_name("select")[2]
Select(qu).select_by_visible_text("碾子山区")
#driver.find_element_by_id("add-new-area-select").find_element_by_css_selector("[value='230000']").click()
#driver.find_element_by_css_selector("[value='230100']").click()
#driver.find_element_by_css_selector("[value='230101']").click()
driver.find_element_by_name("address[address]").send_keys("C座5楼")
driver.find_element_by_name("address[zipcode]").send_keys("050400")
driver.find_element_by_class_name("aui_state_highlight").click()
#标签名定位，重复的概率较大   input   ul   li
#学selenium主要kan标签，标签测试本质