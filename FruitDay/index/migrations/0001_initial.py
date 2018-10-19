# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-30 05:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='商品名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='商品价格')),
                ('spec', models.CharField(max_length=30, verbose_name='商品规格')),
                ('picture', models.ImageField(upload_to='static/upload/goods', verbose_name='商品图片')),
                ('isActive', models.BooleanField(default=True, verbose_name='销售中')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='类别名称')),
                ('desc', models.TextField(null=True, verbose_name='描述')),
                ('picture', models.ImageField(upload_to='static/upload/goodsType', verbose_name='类别图片')),
            ],
            options={
                'verbose_name': '商品类别',
                'verbose_name_plural': '商品类别',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uphone', models.CharField(max_length=11, verbose_name='手机号')),
                ('upwd', models.CharField(max_length=18, verbose_name='密码')),
                ('uname', models.CharField(default='匿名', max_length=30, verbose_name='用户名')),
                ('uemail', models.EmailField(max_length=254, null=True, verbose_name='邮箱')),
                ('isActive', models.BooleanField(default=True, verbose_name='激活')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='goodsType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.GoodsType', verbose_name='商品类别'),
        ),
    ]