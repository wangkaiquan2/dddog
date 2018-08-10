from django.db import models
from users.models import Users


class Attentions(models.Model):
    """关注"""
    user = models.ForeignKey(Users, verbose_name='关注人', related_name='user')
    attentions = models.ForeignKey(Users, verbose_name='被关注人', related_name='attention')
    utime = models.DateTimeField(verbose_name='关注时间', auto_now=True)
    is_cancel = models.BooleanField(verbose_name='是否取消', default=0)
