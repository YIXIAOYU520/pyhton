import json
import unittest
from parameterized import parameterized
from api.第三方车辆进出场API import API
import random


#参数化
def bulid_test():
    file="../date/第三方车场.json"
    test_data=[]
    with open(file,encoding="utf-8") as f:
        json_data=json.load(f)
        for case_data in json_data:
            a = random.randint(1000, 90000000)
            msgId=a
            parkId=case_data.get("parkId")
            plateNumber=case_data.get("plateNumber")
            plateNumberColor=case_data.get("plateNumberColor")
            crossNum=case_data.get("crossNum")
            crossName=case_data.get("crossName")
            passType=case_data.get("passType")
            passTime=case_data.get("passTime")
            merchant=case_data.get("merchant")
            timestamp=case_data.get("timestamp")
            sign=case_data.get("sign")
            test_data.append((msgId,parkId,plateNumber,plateNumberColor,crossNum,crossName,passType,passTime,merchant,timestamp,sign))
        return test_data


class YongLi(unittest.TestCase):
    #前置处理
    def setUp(self) -> None:
        #实例化对象
        self.api=API()
    def tearDown(self):
        print("后置处理")
    @parameterized.expand(bulid_test())
    def test01(self,msgId,parkId,plateNumber,plateNumberColor,crossNum,crossName,passType,passTime,merchant,timestamp,sign):

        resson=self.api.jcc(msgId,parkId,plateNumber,plateNumberColor,crossNum,crossName,passType,passTime,merchant,timestamp,sign)
        token=resson.json()["content"]
        if resson.json()["msg"]=="验签失败":
            resson = self.api.jcc(msgId, parkId, plateNumber, plateNumberColor, crossNum, crossName, passType, passTime,
                                  merchant, timestamp, token)
            print(resson.json())
        elif resson.json()["msg"]=="msgId错误或者已存在":
            a=random.randint(1000, 90000000)
            resson = self.api.jcc(a, parkId, plateNumber, plateNumberColor, crossNum, crossName, passType, passTime,
                                  merchant, timestamp, token)
            token = resson.json()["content"]
            if resson.json()["msg"]=="验签失败":
                resson = self.api.jcc(a, parkId, plateNumber, plateNumberColor, crossNum, crossName, passType, passTime,
                                  merchant, timestamp, token)
                print(resson.json())
            elif resson.json()["msg"] == "success":
                print(resson.json())
            elif resson.json()["msg"] == "没有该车牌的进场记录":
                print(resson.json())
            else:
                print("其他问题")
        elif resson.json()["msg"]=="success":
            print(resson.json())
        elif resson.json()["msg"]=="没有该车牌的进场记录":
            print(resson.json())
        else:
            print("其他问题")



