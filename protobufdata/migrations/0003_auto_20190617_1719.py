# Generated by Django 2.2.2 on 2019-06-17 09:19

from django.db import migrations, models
import time


class Migration(migrations.Migration):

    dependencies = [
        ('protobufdata', '0002_auto_20190617_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='notreal',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='commodity',
            name='real',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='hashCode',
            field=models.CharField(db_index=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='securityCode',
            field=models.CharField(db_index=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='source',
            name='time',
            field=models.IntegerField(default=time.time, verbose_name='更新时间戳'),
        ),
    ]
