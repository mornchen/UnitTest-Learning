# 1. 导包
import unittest

# 2. 自定义测试类，需要继承 unittest 模块中的 TestCase 类即可
class TestDemo1(unittest.TestCase):
    # 3. 书写测试方法，即 用例代码。目前没有真正的用例代码，使用 print 代替
    # 书写要求，测试方法必须以 test 开头
    def testMethod1(self):
        print('测试方法 1')

    def testMethod2(self):
        print('测试方法 2')

# 4. 执行用例（方法）
# 4.1 将光标放在 类名的后面运行，会执行类中的所有的测试方法
# 4.2 将光标放在 方法名的后面运行，只执行当前的方法