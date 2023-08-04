'''TestLoader 的使用'''
# 1. 导包
import unittest

# 2. 使用默认的加载对象并加载用例
suite = unittest.defaultTestLoader.discover('./', 'test04*.py')

# # 3. 实例化 运行对象
# runner = unittest.TextTestRunner()

# # 4. 运行对象执行套件对象
# runner.run(suite)

# 可以将 3 4 步合并为一步
unittest.TextTestRunner().run(suite)