import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        '''每个方法执行之前都会调用的方法'''
        print('输入网址...')
    
    def tearDown(self):
        '''每个方法执行之后都会调用的方法'''
        print('关闭页面...')
    
    @classmethod
    def setUpClass(cls):
        '''每个类执行之前都会调用的方法'''
        print('------1. 打开浏览器')

    @classmethod
    def tearDownClass(cls):
        '''每个类执行之后都会调用的方法'''
        print("------5. 关闭浏览器")

    def test_1(self):
        print('输入正确用户名密码验证码，点击登录 1')
    
    def test_2(self):
        print('输入错误用户名密码验证码，点击登录 2')