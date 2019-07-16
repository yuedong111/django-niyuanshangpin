from django.shortcuts import render, HttpResponse
from protobufdata.models import Company, Commodity, Source, CommodityCategory
from fangniyuan.settings import RES_DATA as res_data
from .login import check_login
# Create your views here.


@check_login
def review(request):
    if request.method == 'POST':
        tem = request.POST
        company = Company.objects.create()
        company.username = tem["username"]
        company.password = tem["password"]
        company.companyName = tem["companyName"]
        company.category = tem["hangye"]
        company.phone = tem["phone"]
        company.area = tem.get("area")
        company.status = 1
        try:
            company.save()
            res_data["msg"] = "插入数据库成功"
            res_data.get("data").update(tem)
        except Exception as e:
            res_data["status"] = 2
            res_data["msg"] = "失败"
            res_data["data"] = {"msg": e}
        return render(request, "upload_review.html", {"message": res_data["msg"]})
    res_data["status"] = 3
    res_data["msg"] = "不支持get方式"
    return render(request, "upload_review.html")
