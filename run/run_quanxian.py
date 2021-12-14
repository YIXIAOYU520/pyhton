import unittest
from scripts.quanxian1 import yonlgi
from tools.HTMLTestRunner import HTMLTestRunner
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(yonlgi))
report="../report/quanxian.html"
with open(report,"wb") as f:
    runner=HTMLTestRunner(f,title="测试报告")
    runner.run(suite)