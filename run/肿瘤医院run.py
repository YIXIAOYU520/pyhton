import unittest
import time
from scripts.肿瘤医院script import yongli
from tools.HTMLTestRunner import HTMLTestRunner
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(yongli))
report="../report/肿瘤医院.html"
with open(report,"wb") as f:
    runner=HTMLTestRunner(f,title="测试报告")
    runner.run(suite)
