# Generated by Django 2.2.2 on 2020-01-13 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_auto_20200113_0353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='client',
        ),
        migrations.RemoveField(
            model_name='people',
            name='flag',
        ),
        migrations.RemoveField(
            model_name='people',
            name='user_visits',
        ),
    ]
