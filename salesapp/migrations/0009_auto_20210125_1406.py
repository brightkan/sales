# Generated by Django 3.1.1 on 2021-01-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesapp', '0008_auto_20210125_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='amount_in_words',
            field=models.CharField(max_length=100),
        ),
    ]
