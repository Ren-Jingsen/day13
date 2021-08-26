'''
    专门生成测试报告
    1.HTMLTESTRUNER
        联网安装


'''

from HTMLTestRunner import HTMLTestRunner
import unittest

test = unittest.defaultTestLoader.discover(r"E:\python proj\day13", pattern="*test.py")

# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器报告",
    description="这是计算机加法的测试报告",
    verbosity=1,
    stream=open(file="计算机测试报告.html", mode="w+", encoding="utf-8")
)

# 3.让运行期运行用例，并生成测试报告
runner.run(test)
