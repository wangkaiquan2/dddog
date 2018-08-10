from django.db import models
from users.models import Users
from releases.models import ServiceOrders


class Comments(models.Model):
    """评论"""
    user = models.ForeignKey(Users, verbose_name='评论者')
    order = models.ForeignKey(ServiceOrders, verbose_name='评论订单')
    content = models.CharField(verbose_name='评论内容', max_length=400)
    fraction = models.IntegerField(verbose_name='分数')
    ctime = models.DateTimeField(verbose_name='评论时间', auto_now=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=0)

    def __str__(self):
        return self.content
