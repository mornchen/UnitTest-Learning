import unittest
from test01_login import login

class TestLoginFunction(unittest.TestCase):

    def test_username_password_ok(self):
        '''正确的用户名和密码：admin, 123456, 登录成功'''
        if login('admin', '123456') == '登录成功':
            print('pass')
        else:
            print('fail')

    def test_username_error(self):
        '''错误的用户名：root, 123456, 登录失败'''
        if login('root', '123456') == '登录失败':
            print('pass')
        else:
            print('fail')
    def test_password_error(self):
        '''错误的密码：admin, 123123, 登录失败'''
        if login('admin', '123123') == '登录失败':
            print('pass')
        else:
            print('fail')
    
    def test_username_password_error(self):
        '''错误的用户名和密码：root, 123123, 登录失败'''
        if login('root', '123123') == '登录失败':
            print('pass')
        else:
            print('fail')

if __name__ == '__main__':
    unittest.main()
