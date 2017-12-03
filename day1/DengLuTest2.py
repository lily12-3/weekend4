#1.打开浏览器
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/")
#2.点击登陆链接
driver.find_element_by_link_text("登录").click()
#从浏览器中的所有窗口中，排除第一个窗口
#把selenium切换到第二个窗口
cwh = driver.current_window_handle
whs = driver.window_handles
#item表示集合中的每一个元素
for item in whs:
    if item == cwh:
        driver.close()
    else:
        driver.switch_to.window(item)
#3.输入用户名和密码
driver.find_element_by_id("username").send_keys("sun1")
driver.find_element_by_id("password").send_keys("123456")

#4.点击登陆按钮
driver.find_element_by_class_name("login_btn").click()