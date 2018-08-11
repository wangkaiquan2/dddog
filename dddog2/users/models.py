from django.db import models
from administrator.models import Limits


class Users(models.Model):
    """用户"""
    uname = models.CharField(verbose_name='用户名', max_length=24, unique=True, null=True)
    password = models.CharField(verbose_name='密码', max_length=200, null=True)
    avatar = models.CharField(verbose_name='头像', max_length=200)
    is_active = models.BooleanField(verbose_name='启用壮态', default=1)
    ctime = models.DateTimeField(verbose_name='注册时间', auto_now_add=True)
    id_card = models.CharField(verbose_name='身份证', max_length=18)
    name = models.CharField(verbose_name='姓名', max_length=18)
    picture = models.CharField(verbose_name='图片', max_length=200)
    address = models.CharField(verbose_name='地址', max_length=200)
    phone = models.CharField(verbose_name='联系方式', max_length=48)
    ulimits = models.ManyToManyField(Limits, verbose_name='用户权限')

    def __str__(self):
        return self.uname


class Groups(models.Model):
    """用户组"""
    gname = models.CharField(verbose_name='组名', max_length=18)
    gmark = models.CharField(verbose_name='组标识', max_length=18, unique=True)
    is_active = models.BooleanField(verbose_name='是否启用', default=1)
    ctime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    gusers = models.ManyToManyField(Users, verbose_name='组用户')
    glimits = models.ManyToManyField(Limits, verbose_name='组权限')

    def __str__(self):
        return self.gname
