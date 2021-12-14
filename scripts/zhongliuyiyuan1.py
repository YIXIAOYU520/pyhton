import json
import unittest
import requests
from api.zhongliuyiyuan import Api
from parameterized import parameterized
import random
def build_data():
    file="../date/index.json"
    test_data=[]
    with open(file,encoding="utf-8") as f:
        json_date=json.load(f)
        for case_data in json_date:
            b = random.randint(11111,99999)
            plateNumber=b
            phone=case_data.get("phone")
            name=case_data.get("name")
            parkId=case_data.get("parkId")
            subDate=case_data.get("subDate")
            subTime=case_data.get("subTime")
            startTime=case_data.get("startTime")
            endTime=case_data.get("endTime")
            a = random.randint(100000, 999999)
            seriaNo=a
            remark=case_data.get("remark")
            merchant=case_data.get("merchant")
            sign=case_data.get("sign")
            timestamp=case_data.get("timestamp")
            SubId=case_data.get("SubId")
            test_data.append((plateNumber,phone,name,parkId,subDate,subTime,startTime,endTime,seriaNo,
                               remark,merchant,sign,timestamp,SubId))
        return test_data

class yongli(unittest.TestCase):
    def setUp(self) -> None:
        self.api=Api()
    def tearDown(self):
        print("后置处理")
    @parameterized.expand(build_data())
    def test01(self,plateNumber,phone,name,parkId,subDate,subTime,startTime,endTime,
               seriaNo,remark,merchant,sign,timestamp,SubId):
        reseon=self.api.yuyue(plateNumber,phone,name,parkId,subDate,subTime,startTime,endTime,seriaNo,
              remark,merchant,sign,timestamp)
        token = reseon.json()["content"]
        if reseon.json()["content"] !=None:
            reseon = self.api.yuyue(plateNumber, phone, name, parkId, subDate, subTime, startTime, endTime, seriaNo,
                                    remark, merchant, token, timestamp)
            self.assertIn("success", reseon.json().get("msg"))
            print(reseon.json())
        else:
            print("车位预约token不存在")
        reseon=self.api.quxiao(SubId,remark,merchant,sign,timestamp)
        token = reseon.json()["content"]
        reseon=self.api.quxiao(SubId,remark,merchant,token,timestamp)
        print(reseon.json())
        self.assertIn("success", reseon.json().get("msg"))
        reseon=self.api.zhuangtai(SubId,merchant,timestamp,sign)
        token=reseon.json()["content"]
        reseon=self.api.zhuangtai(SubId,merchant,timestamp,token)
        print(reseon.json())
        self.assertIn("success", reseon.json().get("msg"))
        reseon=self.api.shuliang(parkId,subDate,merchant,sign,timestamp)
        token=reseon.json()["content"]
        reseon=self.api.shuliang(parkId,subDate,merchant,token,timestamp)
        print(reseon.json())
        self.assertIn("success", reseon.json().get("msg"))

