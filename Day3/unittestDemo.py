# coding=utf-8
#测试框架是干什么用的
#最只要的用途是组织和执行测试用例
#1.导入unittest框架
import unittest
#java中类名和文件名的关系类名和文件名是一样的
#python中的可以一样，推荐文件名首字母小写，类名首字母大写
#继承unittest中的父类
#python中的继承直接用小括号表示
#testcase是测试用例的意思，我们就在unittestDemo中编写测试用例
class UnittestDemo(unittest.TestCase):
 #3.首先要重写父类中的方法setUp和tesrDown方法
 #def是方法的关键字
 #setUp是创建的意思
#类似与手动测试中的预置条件
    def setUp(self):
        print("这个方法将会在测试用例执行前先执行")
    def tearDown(self):
        print("这个方法将会在测试用例方法之后执行")
#4.编写测试用例方法
#只有以test开头命名的方法，才是测试用例方法
#测试用例方法可以直接被运行
# 普通方法不能直接运行，只有被调用才能执行
    def test_log_in(self):
        print("登陆测试用例")
        self.zhu_ce()
    def zhu_ce(self):
        print("注册测试用例")
    def test_search(self):
        print("搜索测试用例")
#如果你直接执行这个文件，那么就会执行下面的语句
#否则，你执行其他文件时，import这个文件的时候，下面的语句就不会被执行
if __name__ == '__main__':
    #表示执行当前文件中所有的unittest的测试用例
    #unittest.main()
    UnittestDemo().zhu_ce()
