# Generated by Django 2.0.4 on 2018-08-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0004_auto_20180717_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procurementinfo',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=14, null=True),
        ),
    ]
