from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Status(models.IntegerChoices):
    Online = 1, '在线'
    Offline = 2, '离线'


class Server(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='ip地址')
    port = models.PositiveIntegerField(verbose_name='端口')
    username = models.CharField(max_length=255, verbose_name='用户名')
    password = models.CharField(max_length=255, verbose_name='密码')
    status = models.IntegerField(choices=Status.choices, verbose_name='状态')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='server')
