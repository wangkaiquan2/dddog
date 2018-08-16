from django.db import models
from users.models import Users


class States(models.Model):
    """订单壮态"""
    sname = models.CharField(verbose_name='状态名', max_length=18)
    smark = models.CharField(verbose_name='壮态标记', max_length=18, unique=True)

    def __str__(self):
        return self.sname


class Services(models.Model):
    """服务表"""
    METHODS = (
        (6, '到店服务'),
        (1, '上门服务'),
        (2, '场所约见'),
        (3, '电话服务'),
        (4, '视频服务'),
        (5, '其他方式'),
    )

    UNITS = (
        (5, '次'),
        (1, '小时'),
        (2, '天'),
        (3, '件'),
        (4, '自定义'),
    )

    ROLES = (
        (1, '需求方'),
        (2, '提供方'),
    )
    users = models.ForeignKey(Users)
    service_number = models.CharField(verbose_name='服务单号', max_length=18)
    role = models.BooleanField(verbose_name='角色', choices=ROLES)
    method = models.IntegerField(verbose_name='服务方式', choices=METHODS)
    title = models.CharField(verbose_name='标题', max_length=18)
    details = models.CharField(verbose_name='详细介绍', max_length=400)
    appoint_time = models.CharField(verbose_name='预约时间', max_length=100)
    remark = models.CharField(verbose_name='备注', max_length=100)
    area = models.CharField(verbose_name='服务地点', max_length=100)
    price = models.FloatField(verbose_name='服务价格')
    unit = models.IntegerField(verbose_name='价格单位', choices=UNITS)
    is_release = models.BooleanField(verbose_name='是否发布', default=1)
    utime = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    def __str__(self):
        return self.service_number


class ServiceOrders(models.Model):
    """需求订单"""
    service_orders_number = models.CharField(verbose_name='订单单号', max_length=18)
    service_number = models.CharField(verbose_name='服务单号', max_length=18)
    provider = models.CharField(verbose_name='服务提供方', max_length=24)
    demand = models.CharField(verbose_name='服务需求方', max_length=24)
    method = models.CharField(verbose_name='类别', max_length=9)
    title = models.CharField(verbose_name='标题', max_length=18)
    details = models.CharField(verbose_name='详细介绍', max_length=400)
    appoint_time = models.CharField(verbose_name='预约时间', max_length=100)
    remark = models.CharField(verbose_name='备注', max_length=100)
    area = models.CharField(verbose_name='服务地点', max_length=100)
    price = models.FloatField(verbose_name='服务价格')
    unit = models.CharField(verbose_name='价格单位', max_length=18)
    ctime = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_complate = models.BooleanField(verbose_name='是否完成', default=0)
    states = models.ManyToManyField(States)

    def __str__(self):
        return self.service_orders_number
