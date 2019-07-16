from django.shortcuts import render, HttpResponse
from .models import Company, Commodity, CommodityCategory, Source, Source1, Source2, Source3, Source4, Source5, Source6, \
    Source7, Source8, Source9, Source10, Source11, Source12, Source13, Source14, Source15, Source16, Source17, Source18, \
    Source19
import json
from fangniyuan.settings import RES_DATA as res_data
from django.db.models import Count


# Create your views here.


def query_commidty(request, hash_code="111"):
    # TODO:此接口不需要hashcode,该接口还没用
    hashCode = hash_code
    if request.method == "POST":
        temp = request.POST
        securityCode = temp.get("securityCode")
        com = Commodity.objects.filter(securityCode=securityCode).first()
        if com and hashCode:
            res = {
                "commodityName": com.commodityName,
                "categoryId": com.categoryId.categoryId,
                "attributes": json.loads(com.attributes),
                "price": com.price,
                "companyId": com.companyId.companyId
            }
            res_data["status"] = 1
            res_data["msg"] = "查询成功"
            res_data.get("data").update(res)
        else:
            res_data["status"] = 4
            res_data["msg"] = "无此商品"
            # TODO: 传入参数到前段
        return render(request, "commodity/index.html", {"data": res_data, "hash_code": hash_code})
    else:
        return render(request, "commodity/index.html")


def check_commodity(request):
    index = request.path.find("ck/")
    hashcode = request.path[index + 3:]
    if request.method == "POST":
        temp = request.POST
        securityCode = temp.get("securityCode")
        ip = request.META.get("REMOTE_ADDR")
        user = request.user
        com = Commodity.objects.filter(hashCode=hashcode, securityCode=securityCode).first()
        if com:
            commodity_name = com.commodityName
            categoryId = com.categoryId.categoryId
            index = int(categoryId) % 20
            target = "Source"
            if index:
                target = target + str(index)
            Soe = globals().get(target)
            sou = Soe.objects.filter(ip=ip, securityCode=securityCode).first()
            if sou:
                res_data["status"] = 2
                res_data["msg"] = com.notreal
                s = Soe(ip=ip, securityCode=securityCode, operation="查询商品安全码", operatorPerson=user,
                           name=commodity_name,
                           commodityId=com)
                s.save()
            else:
                res_data["msg"] = com.real
                s = Soe(ip=ip, securityCode=securityCode, operation="查询商品安全码", operatorPerson=user,
                           name=commodity_name,
                           commodityId=com, operationStatus=1)
                s.save()
                res = {
                    "commodityName": com.commodityName,
                    "categoryId": com.categoryId.categoryId,
                    "attributes": json.loads(com.attributes),
                    "price": com.price,
                    "companyId": com.companyId.companyId
                }
                res_data["status"] = 1
                res_data.get("data").update(res)
                return render(request, "commodity/index.html",
                              {"data": res_data, "message": res_data["msg"], "hash_code": hashcode})
        else:
            res_data["status"] = 4
            res_data["msg"] = "没有此商品"
    else:
        res_data["status"] = 3
        res_data["msg"] = ""
    return render(request, "commodity/index.html",
                  {"data": res_data, "message": res_data["msg"], "hash_code": hashcode})


def emu_commodity(request):
    coms = CommodityCategory.objects.filter().all()
    hashCodes = map(lambda x: Commodity.objects.filter(categoryId=x.categoryId).values("hashCode").distinct(), coms)
    commodities = []
    for item in hashCodes:
        for com in item:
            temp = Commodity.objects.filter(hashCode=com.get("hashCode")).first()
            commodities.append(temp)
    return render(request, "commodities.html", {"commodities": commodities})
