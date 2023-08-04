import unittest

version = 30

class TestDemo(unittest.TestCase):
    @unittest.skip("没有什么原因，就是不想执行")
    def test_1(self):
        print("测试方法 1")
    
    @unittest.skipIf(version >= 30, "版本大于30，不用测试")
    def test_2(self):
        print("测试方法 2")
    
    def test_3(self):
        print("测试方法 3")

 # 运行测试用例
if __name__ == '__main__':
    unittest.main()