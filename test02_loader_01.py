'''TestLoader 的使用'''
# 1. 导包
import unittest

# 2. 实例化测试加载对象并添加用例 ---> 得到的是 suite 对象
# unittest.TestLoader().discover('用例所在的路径', '用例的代码文件名')
# 用例所在的路径，建议使用相对路径。
# 用例的代码文件名可以使用 *（任意多个任意字符）通配符
suite = unittest.TestLoader().discover('./case', 'test*.py')
# suite = unittest.TestLoader().discover('./case', '*case*.py')
# suite = unittest.TestLoader().discover('./case', '*test*')
# suite = unittest.TestLoader().discover('./case', '*case01.py')


# # 3. 实例化 运行对象
# runner = unittest.TextTestRunner()

# # 4. 运行对象执行套件对象
# runner.run(suite)

# 可以将 3 4 步合并为一步
unittest.TextTestRunner().run(suite)