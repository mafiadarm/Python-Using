# Generated by Django 2.2.2 on 2020-01-13 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0004_auto_20200113_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='come_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
