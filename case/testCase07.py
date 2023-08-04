import unittest

from test01_login import login


class TestLoginFunction(unittest.TestCase):

    def test_login_success(self):
        # 正确的用户名和密码：admin, 123456, 登录成功
        result = login('admin', '123456')
        self.assertEqual(result, '登录成功')

    def test_login_fail_01(self):
        # 错误的用户名：root, 123456, 登录失败
        result = login('root', '123456')
        self.assertEqual(result, '登录失败')

    def test_login_fail_02(self):
        # 错误的密码：admin, 123123, 登录失败
        result = login('admin', '123123')
        self.assertEqual(result, '登录失败')

    def test_login_fail_03(self):
        # 错误的用户名和密码：root, 123123, 登录失败
        result = login('root', '123123')
        self.assertEqual(result, '登录失败')


if __name__ == '__main__':
    unittest.main()
