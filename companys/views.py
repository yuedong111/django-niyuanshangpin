from django.shortcuts import render, HttpResponse
from protobufdata.models import CommodityCategory, Company, Commodity
import json
import hashlib
from fangniyuan.settings import RES_DATA as res_data
import random
from functools import reduce
from django.db import transaction
from .login import check_login as check_company
# Create your views here.


# def check_company(func):
#     def wrapper(request, *args, **kwargs):
#         if request.COOKIES.get("Authorization") == "Y6GT6rqg6l+jqvcJfKBK9gQehLOBWndYxyknhcUZm/y+aUYIa/UcMA==":
#             return func(request, *args, **kwargs)
#         else:
#             res_data["status"] = 404
#             res_data["msg"] = "你没有权限"
#             return HttpResponse(json.dumps(res_data, ensure_ascii=False), content_type="application/json,charset=utf-8")
#     return wrapper


@check_company
def up_commodity_cate(request):
    if request.method == 'POST':
        tem = request.POST
        cid = Company.objects.get(companyId=tem["companyId"])
        ccg = CommodityCategory(companyId=cid, categoryName=tem["categoryName"], attributes=tem["attributes"])
        try:
            ccg.save()
            res_data["msg"] = "插入数据库成功"
            res_data.get("data").update(tem)
        except Exception as e:
            res_data["status"] = 2
            res_data["msg"] = "失败"
            res_data["data"] = {"msg": e}
        return HttpResponse(json.dumps(res_data, ensure_ascii=False), content_type="application/json,charset=utf-8")
    res_data["status"] = 3
    res_data["msg"] = "不支持get方式"
    return HttpResponse(json.dumps(res_data, ensure_ascii=False), content_type="application/json,charset=utf-8")


@check_company
def up_commodity(request):
    if request.method == 'POST':
        tem = request.POST
        cid = Company.objects.get(companyId=tem.get("companyId"))
        cte = CommodityCategory.objects.get(categoryId=tem.get("categoryId"))
        if not cid:
            res_data["msg"] = "没有该公司"
        if not cte:
            res_data["msg"] = "没有该商品类别"
        if cid and cte:
            ccg = Commodity(companyId=cid, categoryId=cte, commodityName=tem["commodityName"],
                            attributes=tem["attributes"])
            try:
                ccg.save()
                res_data["msg"] = "插入数据库成功"
                res_data.get("data").update(tem)
            except Exception as e:
                res_data["status"] = 2
                res_data["msg"] = "失败"
                res_data["data"] = {"msg": "插入数据库失败"}
        return render(request, "company/add_commodity.html", {"message": res_data["msg"]})
    res_data["status"] = 3
    res_data["msg"] = "不支持get方式"
    return render(request, "company/add_commodity.html", {"message": res_data["msg"]})


@check_company
def gen_hash(request):
    if request.method == "POST":
        temp = request.POST
        commodity_name = temp.get("commodityName")
        company_id = temp.get("companyId")
        coms = Commodity.objects.filter(companyId=company_id, commodityName=commodity_name)
        if coms:
            count = len(coms)
            seed = commodity_name
            res = hashlib.sha256(seed.encode("utf-8")).hexdigest()
            res = res + str(count)
            try:
                coms.update(hashCode=res)
                res_data["msg"] = "生成商品码成功"
                res_data.get("data").update(temp)
            except Exception as e:
                print(e)
                res_data["status"] = 2
                res_data["msg"] = "失败"
                res_data["data"] = {"msg": "更新hash失败"}
        else:
            res_data["status"] = 0
            res_data["msg"] = "没有该商品"
            res_data["data"] = {}
        return render(request, "company/gen_code.html", {"message": res_data["msg"]})
    res_data["status"] = 3
    res_data["msg"] = "不支持get方式"
    return render(request, "company/gen_code.html")








