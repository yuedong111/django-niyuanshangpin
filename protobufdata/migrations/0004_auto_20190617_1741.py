# Generated by Django 2.2.2 on 2019-06-17 09:41

from django.db import migrations, models
import protobufdata.models


class Migration(migrations.Migration):

    dependencies = [
        ('protobufdata', '0003_auto_20190617_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='securityCode',
            field=models.CharField(db_index=True, default=protobufdata.models.random_num6, max_length=10),
        ),
    ]
