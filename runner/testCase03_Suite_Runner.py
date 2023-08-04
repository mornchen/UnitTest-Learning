'''
学习 TestSuite 和 TestRunner 的使用
'''
# 1. 导包（unittest）
import unittest

# 2. 实例化（创建对象）套件对象
from case.testCase01 import TestDemo1
from case.testCase02 import TestDemo2

suite = unittest.TestSuite()

# 3. 使用套件对象添加用例方法
# 方式一：套件对象.addTest(测试类名('方法名'))   # 建议测试类名和方法名直接复制，不要手敲
# suite.addTest(TestDemo1('testMethod1'))
# suite.addTest(TestDemo1('testMethod2'))
# suite.addTest(TestDemo2('testMethod3'))
# suite.addTest(TestDemo2('testMethod4'))

# 方式二：将一个测试类中的所有方法进行添加
# 套件对象.addTest(unittest.makeSuite(测试类名))
# 缺点：函数makeSuite()没有代码提示
suite.addTest(unittest.makeSuite(TestDemo1))
suite.addTest(unittest.makeSuite(TestDemo2))

# 4. 实例化运行对象
runner = unittest.TextTestRunner()

# 5. 使用运行对象去执行套件对象
# 运行对象.run(套件对象)
runner.run(suite)