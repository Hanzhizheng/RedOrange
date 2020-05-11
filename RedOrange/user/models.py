from django.db import models
from django.contrib.auth.models import AbstractUser
from ads.models import FKeyPartyAMixin


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
    name = models.CharField(
        '名字',
        max_length=10,
        help_text='名字',
    )
    nickname = models.CharField(
        '昵称',
        max_length=10,
        default='',
        blank=True,
        help_text='昵称',
    )
    juices = models.PositiveSmallIntegerField(
        '积分数',
        default=0,
        blank=True,
        help_text='积分数',
    )
    checked_in = models.BooleanField(
        '是否打卡',
        default=False,
        blank=True,
        help_text='是否打卡',
    )
    brithday = models.DateField(
        '出生日期',
        null=True,
        help_text='出生日期',
    )
    SEX = (
        (1, '男'),
        (0, '女'),
        (2, '未知')
    )
    sex = models.IntegerField(
        '标识符申请状态',
        choices=SEX,
        default=2,
        help_text='标识符申请状态',
    )

    @property
    def age(self):
        return 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class FKeyUserMixin(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='用户',
        on_delete=models.CASCADE,
        help_text='用户',
    )
    class Meta:
        abstract = True


class JobCard(FKeyPartyAMixin, FKeyUserMixin):
    position = models.CharField(
        '岗位',
        max_length=10,
        help_text='岗位',
    )
    is_admin = models.BooleanField(
        '是否是管理员',
        default=False,
        blank=True,
        help_text='是否是管理员',
    )
    is_verified = models.BooleanField(
        '是否认证身份',
        default=False,
        blank=True,
        help_text='是否认证身份',
    )

    class Meta:
        verbose_name = '工作卡'
        verbose_name_plural = verbose_name


class SocialCard(FKeyUserMixin):

    class Meta:
        verbose_name = '社交卡'
        verbose_name_plural = verbose_name 