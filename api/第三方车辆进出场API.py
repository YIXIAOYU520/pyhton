#导包
import requests
class API:
    def __init__(self):
        self.url="https://test.easy-parking.cn/easypark/parking-service/api-record/recordReport"
    def jcc(self,msgId,parkId,plateNumber,plateNumberColor,crossNum,crossName,passType,passTime,merchant,timestamp,sign):
        json={
            "msgId": msgId,
            "parkId": parkId,
            "plateNumber": plateNumber,
            "plateNumberColor": plateNumberColor,
            "crossNum": crossNum,
            "crossName": crossName,
            "passType": passType,
            "passTime": passTime,
            "merchant": merchant,
            "timestamp": timestamp,
            "sign": sign
        }
        return requests.post(url=self.url,json=json)