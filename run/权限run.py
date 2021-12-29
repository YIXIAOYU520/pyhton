import unittest
from scripts.权限script import yongli
from tools.HTMLTestRunner import HTMLTestRunner
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(yongli))
report="../report/权限.html"
with open(report,"wb") as f:
    runner=HTMLTestRunner(f,title="测试报告")
    runner.run(suite)