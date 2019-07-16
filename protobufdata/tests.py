from django.test import TestCase

# Create your tests here.
import requests
import json

data = {"username": "cll",
        "password": "123456",
        "phone": "121231213",
        "hangye": "sjdlsss",
        "area": "chongqing",
        "hangye": "slds",
        "companyName": "sdl"}

attribute = {"容量": "500ml", "产地": "四川"}
data_comcate = {
    "companyId": 1,
    "categoryName": "矿泉水",
    "attributes": json.dumps(attribute, ensure_ascii=False),
    "price": '1.00'
}
data_commodity = {
    "companyId": 1,
    "commodityName": "矿泉水",
    "attributes": json.dumps(attribute, ensure_ascii=False),
    "categoryId": "1",
    "price": "2"
}
genhash = {
    "commodityName": "矿泉水",
    "companyId": 1,
}
hash = {"hashCode": "6b1311e9a899a0d494a7e3dc812df01e331bcdc411730d0062e4b657e32c27c635"}
hash_com = {"hashCode": "6b1311e9a899a0d494a7e3dc812df01e331bcdc411730d0062e4b657e32c27c635",
            }
# r = requests.post("http://127.0.0.1:8000/user/", data=data)
# print(r.text)
# r = requests.post("http://127.0.0.1:8000/company/", data=data_comcate)
# print(r.text)
# for _ in range(10):
# r = requests.post("http://127.0.0.1:8000/company/commodity/", data=data_commodity)
# print(r.text)
# r = requests.post("http://127.0.0.1:8000/company/hashgen/", data=genhash)
# print(r.text)
# r = requests.post("http://127.0.0.1:8000/user/commodity/", data=hash)
# print(r.text)
# r = requests.post("http://127.0.0.1:8000/user/commoditycheck/", data=hash_com)
# print(r.text)
r = requests.get("http://127.0.0.1:8000/user/all_commodity/")
print(r.text)