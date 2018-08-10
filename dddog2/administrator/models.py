from django.db import models


class Limits(models.Model):
    """权限"""
    limit = models.CharField(verbose_name='权限标识', max_length=18, unique=True)
    limit_description = models.CharField(verbose_name='权限描述', max_length=18)

    def __str__(self):
        return self.limit_description
