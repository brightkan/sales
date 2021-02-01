# Generated by Django 3.1.1 on 2021-01-28 12:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0013_auto_20210128_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracksetting',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 28, 12, 1, 37, 897377, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tracksetting',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2021, 1, 28, 12, 1, 37, 897357, tzinfo=utc)),
        ),
    ]
