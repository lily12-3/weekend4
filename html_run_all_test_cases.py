# coding=utf-8
import os
import smtplib
import time
import unittest
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    f = open(path,'rb')  #具体的内容
    mail_body = f.read()    #读出来
    f.close()
    #要想发邮件，我们要把二进制内容转成MIME格式
    #MIME multipurse多用途   internet  互联网    Mail 邮件    Extension扩展
    #这种格式是对邮件协议的扩展，使邮件不仅支持文本格式，还支持多种格式，比如说图片、音频或者是二进制文件等
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header("自动化测试报告",'utf-8')
    msg['From'] = 'bwftest126@126.com'
    msg['To'] = 'sunnana424@126.com'
    #发邮件的手动步骤
    #1.打开登陆页面,即链接邮箱服务器
    #要想链接服务器,首先必须搞清楚网络传输协议
    #http  https ftp socket
    #发邮件的协议一般有3种,你要先察看下你的邮箱支持那种协议
    #126邮箱支持这3种协议:pop3 smtp imap
    #我们要选一种传输协议,用来发邮件,stmp
    #stmp simple  mail transfui protocol
    smtp = smtplib.SMTP()  #实例化一个smtp的对象
    smtp.connect("smtp.126.com")
    #2.登陆邮箱
    smtp.login('bwftest126@126.com','abc123asd654')
    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp.quit()
    print('email has sent out')
    #如果想用客户端软件或者自己写代码登陆邮箱,很多类型邮箱的服务器是需要单独设置一个客户端授权码
    #设置一个客户端授权码,为了邮箱安全着想
    #因为你们都没有设置授权码,所以发件箱统一用我的
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    suite = unittest.defaultTestLoader.discover('./day5', '*Test.py')
    #unittest.TextTestRunner  文本测试用例运行器
    #现在用html的测试用例运行器
    #html的测试用例运行器最终会生成一个html格式的测试报告
    base_path = os.path.dirname(__file__)
    path = base_path+"/report/report"+now+".html"
    file = open(path, "wb")
    HTMLTestRunner(stream=file, title="海盗商城测试报告", description="测试环境：windows server 2008+chrom").run(suite)
    file.close()
    send_mail(path)
    #这时生成的测试报告只显示类名和方法名，只能给专业的人士看
    #我们应该把相关的手动测试用例的标题加到我们的测试报告中
    #我们自动化测试用例是从手工测试用例中挑出来的，手工测试用例怎么写，我们就怎么编写脚本，所以我们的代码里应该能体现手工测试用例的标题
    #新的测试报告会覆盖原来的测试报告，如果想把原来的测试保存下来怎么做
    #加一个时间戳，按照当前时间计算一个数字，把数字作为文件名的一部分，就避免了文件名重复的部分

