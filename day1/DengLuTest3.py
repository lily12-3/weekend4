#javascript  是一门独立的语言
#要想学好selenium，最重要的三件事：
#1.元素的定位：id    name   class    test
#link_test必须是链接，必须是<a> ,必须是文本
#2.元素的操作：鼠标左键单击click，发送键盘上的按键 send_keys
#3.学好javascript
#用javascript实现窗口切换
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/")
#javascript和python是不同的语言，pycharm是用来写python语言
#怎么在python执行javascript语言
js = 'document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
#js是一个变量，所以不用加引号
driver.execute_script(js)
driver.find_element_by_link_text("登录").click()
#输入用户名和密码
driver.find_element_by_id("username").send_keys("sun1")
driver.find_element_by_id("password").send_keys("123456")
