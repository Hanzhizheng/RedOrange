from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """用户
    """
    phone = models.CharField(
        '联系电话',
        max_length=11,
        unique=True,
        help_text='联系电话',
    )
    avator = models.ImageField(
        '头像',
        upload_to='Avators/',
        default='',
        blank=True,
        help_text='头像',
    )
    nickname = models.CharField(
        '昵称',
        max_length=20,
        default='',
        blank=True,
        help_text='昵称',
    )
    juices = models.SmallIntegerField(
        '积分数',
        default=0,
        blank=True,
        help_text='积分数',
    )

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class FKeyUserMixin():
    user = models.ForeignKey(
        User,
        verbose_name='用户',
        on_delete=models.CASCADE,
        help_text='用户',
    )

    class Meta:
        abstract = True
