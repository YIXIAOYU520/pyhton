import requests
class Api:
    def __init__(self):
        self.url1 = "https://test.easy-parking.cn/easypark/third-service/space/sub"
        self.url2 = "https://test.easy-parking.cn/easypark/third-service/space/cancel"
        self.url3 = "https://test.easy-parking.cn/easypark/third-service/space/queryStatus"
        self.url4 = "https://test.easy-parking.cn/easypark/third-service/space/count"
        self.url5 = "https://test.easy-parking.cn/easypark/cms-service/admin/remission/otherRemissionGrantV2"
    def yuyue(self,plateNumber,phone,name,parkId,subDate,subTime,startTime,endTime,a,
              remark,merchant,sign,timestamp):
        json={
            "plateNumber":plateNumber,
            "phone":phone,
            "name":name,
            "parkId":parkId,
            "subDate":subDate,
            "subTime":subTime,
            "startTime":startTime,
            "endTime":endTime,
            "seriaNo":a,
            "remark":remark,
            "merchant":merchant,
            "sign":sign,
            "timestamp":timestamp
        }
        return requests.post(url=self.url1,json=json)
    def quxiao(self,SubId,remark,merchant,sign,timestamp):
        json={
            "SubId": SubId,
            "Remark": remark,
            "Merchant": merchant,
            "Sign": sign,
            "Timestamp": timestamp
        }
        return requests.post(url=self.url2,json=json)
    def zhuangtai(self,SubId,merchant,timestamp,sign):
        date={
            "subId":SubId,
            "merchant":merchant,
            "timestamp":timestamp,
            "sign":sign
        }
        return requests.get(url=self.url3,params=date)
    def shuliang(self,parkId,subDate,merchant,sign,timestamp):
        data={
            "parkId":parkId,
            "subDate":subDate,
            "merchant":merchant,
            "sign":sign,
            "timestamp":timestamp
        }
        return requests.get(url=self.url4,params=data)
    def jianmianquan(self,merchant,discountNumber,color,phone,orderId,remark,timestamp,plateNumber,remissionId,sign):
        json={
            "merchant":merchant,
            "discountNumber": discountNumber,
            "color": color,
            "phone": phone,
            "orderId": orderId,
            "remark": remark,
            "timestamp": timestamp,
            "plateNumber": plateNumber,
            "remissionId": remissionId,
            "sign": sign
        }
        return requests.post(url=self.url5,json=json)

