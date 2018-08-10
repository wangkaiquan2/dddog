from django.db import models
from user.models import Users
from release.models import Services


class Collect(models.Model):
    """收藏"""
    user = models.ForeignKey(Users)
    collects = models.ForeignKey(Services)
    utime = models.DateTimeField(verbose_name='收藏时间', auto_now=True)
    is_cancel = models.BooleanField(verbose_name='是否取消', default=0)
