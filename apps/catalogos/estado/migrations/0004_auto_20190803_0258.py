# Generated by Django 2.2.2 on 2019-08-03 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0003_auto_20190715_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 3, 2, 58, 6, 859636)),
        ),
    ]