from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserInfo(AbstractUser):
    CHOICES =(
        ("male",u'男'),
        ("female",u'女')
    )
    gender = models.CharField('性别',max_length=8,choices=CHOICES,default='male')
    mobile = models.CharField('电话',max_length=11)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'

    def __str__(self):
        return self.username
