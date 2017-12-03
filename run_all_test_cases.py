# coding=utf-8
import os
import unittest


if __name__ == '__main__':
    #默认的测试用例
    suite = unittest.defaultTestLoader.discover('./day5', pattern='*Test.py')  #一组测试用例  suite
    #文本的测试用例执行器

