# Generated by Django 2.2.1 on 2019-05-19 16:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0005_auto_20190520_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
