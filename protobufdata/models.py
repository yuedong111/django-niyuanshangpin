from django.db import models
import time
import random
from functools import reduce


# Create your models here.


class Company(models.Model):
    companyId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    companyName = models.CharField(max_length=128)
    category = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    status = models.CharField(max_length=10, default="0")

    def __str__(self):
        return self.companyName


def random_num6():
    temp1 = [random.randint(0, 9) for _ in range(6)]
    num = reduce(lambda x, y: str(x) + str(y), temp1)
    return num


class CommodityCategory(models.Model):
    categoryId = models.AutoField(primary_key=True)
    companyId = models.ForeignKey('Company', on_delete=models.CASCADE)
    categoryName = models.CharField(max_length=64)
    attributes = models.CharField(max_length=256)
    price = models.CharField(max_length=10, default=0)


class Commodity(models.Model):
    id = models.AutoField(primary_key=True)
    companyId = models.ForeignKey('Company', on_delete=models.CASCADE)
    categoryId = models.ForeignKey('CommodityCategory', on_delete=models.CASCADE)
    commodityName = models.CharField(max_length=64)
    attributes = models.CharField(max_length=256)
    hashCode = models.CharField(max_length=80, db_index=True)
    securityCode = models.CharField(max_length=10, db_index=True, default=random_num6)
    price = models.CharField(max_length=10, default=0)
    real = models.CharField(max_length=256, default="")
    notreal = models.CharField(max_length=256, default="")
    batch = models.CharField(max_length=30, default="201906180001")


class Source(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source1(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source2(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source3(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source4(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source5(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source6(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source7(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source8(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source9(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source10(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source11(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source12(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source13(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source14(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source15(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source16(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source17(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source18(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")


class Source19(models.Model):
    id = models.AutoField(primary_key=True)
    commodityId = models.ForeignKey('Commodity', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    ip = models.CharField(max_length=32)
    operation = models.CharField(max_length=64)
    operatorPerson = models.CharField(max_length=40)
    securityCode = models.CharField(max_length=10)
    time = models.IntegerField(verbose_name="更新时间戳", default=time.time)
    operationStatus = models.CharField(max_length=10, default="0")
