# Generated by Django 2.2.1 on 2019-05-19 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolists', '0007_todo_starttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.CharField(blank=True, default=datetime.date.today, max_length=20),
        ),
    ]
