# 1. 获取第三方的 测试运行类模块，将其放在代码的目录中
# 2. 导包 unittest
import unittest
from HTMLTestRunner import HTMLTestRunner
from HTMLTestRunnerCN import HTMLTestReportCN

# 3.使用 套件对象，加载对象 去添加用例方法
suite = unittest.defaultTestLoader.discover('./', 'test06_parameterized.py')

# 4.实例化 第三方的运行对象，并运行套件对象
# HTMLTestRunner()
# stream=sys.stdout 测试报告的文件对象（open），注意：要用 wb 打开
# verbosity=1 报告的详细程度，默认 1 为简略报告，2 为详细报告
# title=None 可选，测试报告的标题
# description=None 可选，描述信息，Python 的版本，Pycharm 版本

file = 'test-reports/test06_parameterized_report.html'
with open(file, 'wb') as f:
    runner = HTMLTestRunner(stream=f, verbosity=2, title='test06_parameterized_report')

    # 运行对象执行套件，要写在 with 的缩进中
    runner.run(suite)