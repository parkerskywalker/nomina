# Generated by Django 2.2.2 on 2019-07-16 00:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0002_auto_20190701_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 15, 19, 55, 51, 539965)),
        ),
    ]
