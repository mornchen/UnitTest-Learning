# 1. 导包 unittest/parameterized
import unittest
from parameterized import parameterized
from test01_login import login
import json

# 组织测试数据 [(), (), ()]
# 方法一：在列表里面读取数据
# data = [
#      ('admin', '123456', '登录成功'),
#      ('root', '123456', '登录失败'),
#      ('admin', '123123', '登录失败'),
#      ('root', '123123', '登录失败')
#  ]

# 方法二：在 json 文件里面读取数据
def build_data():
    # 打开存储测试数据的 JSON 文件
    with open('TestData/data.json', encoding='utf-8') as f:
        # 使用 json.load() 方法读取 JSON 数据，结果是一个包含字典的列表 [{}, {}, {}]
        result = json.load(f) # [{}, {}, {}] --> [(), (), ()]
        data = []
        # 遍历 JSON 数据列表，提取用户名、密码和期望结果，并将它们组成元组后添加到 data 列表中
        for i in result: # i {}
            data.append((i.get("username"), i.get("password"), i.get("expect")))
    return data

 # 2. 定义测试类
class TestLogin(unittest.TestCase):
    # 3. 书写测试方法（用到的测试数据使用变量代替）
    # 使用 @parameterized.expand 装饰器将测试数据传递给测试用例方法 test_login
    @ parameterized.expand(build_data())
    def test_login(self, username, password, expect):
        # 使用 self.assertEqual() 断言方法来判断 login 函数返回的结果是否与期望的结果一致
        self.assertEqual(login(username, password), expect)
 
 # 4. 组织测试数据并传参（装饰器 @）


 # 5. 运行测试用例
if __name__ == '__main__':
    unittest.main()