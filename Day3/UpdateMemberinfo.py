#1.登陆
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("sun1")
#Actions 行为，动作的意思
#Chain 链表的意思
#ActionChains表示一组行为和动作
#实现一组动作，按Tab键----输入密码---按回车键---结束
#perform 执行，前面的所有动作都要等到perform这个方法才会开始执行
#所有元素的高级操作，都在ActionChains
#Key这个类封装所有键盘上的特殊键
ActionChains(driver).send_keys(Keys.TAB).send_keys("123456").send_keys(Keys.ENTER).perform()

#2.点击账号设置
driver.find_element_by_link_text("账号设置").click()
#3.点击个人资料
driver.find_element_by_partial_link_text("个人资料").click()
#4.修改个人信息
driver.find_element_by_name("true_name").clear()
driver.find_element_by_name("true_name").send_keys("万里")
#性别
#css属性可以用多个属性组合定位一个元素
#一个元素的多个属性之前不能有空格
driver.find_element_by_css_selector("#xb[value='1']").click()
#java script是一个单独的语言，和python的语法不一样，不能直接在python中执行
#js = 'document.getElementById("date").removeAttribute("readonly")'
#driver.execute_script(js)
#driver.find_element_by_id("date").clear()
#driver.find_element_by_id("date").send_keys("2000-11-21")
#用arguments(参数）改写上面输入
date = driver.find_element_by_id("date")
driver.execute_script('arguments[0].removeAttribute("readonly")',date)
date.clear()
date.send_keys("1980-11-21")
#用selenium调用javascript一共有2个关键字：1.argumens[0]:用python语言代替一部分javascipt
#好处是，有时selenium定位比较容易
#2.return把javascip的执行结果返回给python语言
#好处，有时selenium定位不到的元素，我们用javascipt定位到
#date = driver.execute_script("return document.gerElementById('date')")
#这句话等于 ==clac = driver.find_element_by_id("date")
#date.click()
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("7894561234")
driver.find_element_by_class_name("btn4").click()
#邮件检查不了html代码的弹出框，叫做alert，有单独的方法来处理
time.sleep(3)
#alert空间不是html生成的，所以implicitly_wait对这个空间不管用
#所以就算上面写了implicitly_wait,这个time.sleep（）方法不能省略
#切换到alert的方法，和切换窗口的方法类似
#alert 弹出框，accept 接受，同意，确定   dismiss  拒绝，取消
driver.switch_to.alert.accept()
#driver.switch_to.alert().dismiss()