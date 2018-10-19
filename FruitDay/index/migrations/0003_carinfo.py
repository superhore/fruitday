# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-24 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20180423_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gcount', models.IntegerField(verbose_name='商品数量')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Goods', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Users', verbose_name='用户信息')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
    ]
