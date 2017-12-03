# coding=utf-8
#1.之前的readcsv不能被其他测试用例调用，所以应该给这段代码封装到一个方法里
#2.每个测试用例的路径不同，所以path应该作为参数传入到这个方法中
#4.我们打开了一个文件，但是并没有关闭，最终可能造成内存泄露
import csv
import os
def read(file_name):
    #所有的重复代码的出现，都是程序设计的不合理
    #重复的代码应该单独封装在一个方法里
    current_file_path = os.path.dirname(__file__)
    path = current_file_path.replace("day4", "data/"+file_name)
    #file = open(path,'r')
    #with语句是一个代码块，代码块中的内容都要缩进4个空格
    #with代码块可以自动关闭with中声明的变量
    #因为file文件一旦关闭，里面的数据也随着消失
    #所以单独声明一个列表result，来保存里面的数据
    result = []

    with open(path,'r') as file:
        data_table = csv.reader(file)
        for row in data_table:
            result.append(row)
    return result
        #如果在打开和关闭程序的代码中发生了异常，导致后面的代码不能正常运行
        #file.close()也不执行，这时，文件仍然不能关闭
        #应该用with...as...语句实现文件的关闭
        #file.close()
if __name__ == '__main__':
   # path = r"C:\Users\51Testing\PycharmProjects\weekend4\data\member_info.csv"
    #3.这个路径是绝对路径，我们工作中，一个项目不止一个人编写代码，我们没法统一要求大家都把项目代码放在一个路劲下，因为有的人 会放在D盘
    #这个文件因为在项目中，它的路径也会随着项目变化
    #所以应该在代码中，通过当前代码文件的路径，根据相对位置，找到csv文件
   #所以首先要找到当前文件路径
   #os是操作系统，path是路径  dir是目录  directory  __file__   双下划线的文件是python内置的变量，指的是当前文件
   #print(current_file_path)
   #我们真正想要的路径是csv的路径

  # print(path)
   member_info = read("member_info.csv")
   for row in member_info:
       print(row[0])
   #5.读出数据不是目的，目的是通过数据驱动测试，所以应该把数据作为方法的返回值，方便进一步调用

       os.path.