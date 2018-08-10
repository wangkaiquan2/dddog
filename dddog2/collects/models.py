from django.db import models
from users.models import Users
from releases.models import Services


class Collect(models.Model):
    """收藏"""
    user = models.ForeignKey(Users, verbose_name='用户')
    collects = models.ForeignKey(Services, verbose_name='收藏服务')
    utime = models.DateTimeField(verbose_name='收藏时间', auto_now=True)
    is_cancel = models.BooleanField(verbose_name='是否取消', default=0)
