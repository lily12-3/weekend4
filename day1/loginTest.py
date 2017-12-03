#1.打开浏览器
from selenium import webdriver
#从selenium中导入 网络驱动 用代码来操作浏览器的
driver = webdriver.Chrome()
#2.打开登陆页面
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#3.输入用户名 首先寻找用户名的输入框
#网页上所有可见的都属于element，比如link，按钮，下拉框。。。。
#在叫driver的浏览器上，寻找一个网页元素，如果它的id等于"username"
#并向页面元素中发送键盘上sun这几个按键
driver.find_element_by_id("username").send_keys("sun")
#4.输入密码
driver.find_element_by_id("password").send_keys("123456")
#5.点击登陆按钮
#如果我使用一个方法，这个方法没有提示信息，那么这个方法肯定是不存在的
driver.find_element_by_class_name("login_btn ").click()