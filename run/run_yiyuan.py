import unittest
import time
from scripts.zhongliuyiyuan1 import yongli
from tools.HTMLTestRunner import HTMLTestRunner
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(yongli))
report="../report/zhongliuyiyuan.html"
with open(report,"wb") as f:
    runner=HTMLTestRunner(f,title="测试报告")
    runner.run(suite)
