# Generated by Django 2.2.2 on 2020-01-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20200113_0314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='null', max_length=50, verbose_name='节目名称')),
                ('introduce', models.TextField(default='null', verbose_name='节目介绍')),
                ('score', models.SmallIntegerField(default=0, verbose_name='得分')),
                ('tags', models.ManyToManyField(blank=True, to='vote.Tag', verbose_name='标签')),
            ],
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
