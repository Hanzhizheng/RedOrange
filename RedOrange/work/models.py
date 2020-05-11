from django.db import models
from django.utils.decorators import classproperty

from ads.models import FKeyPartyAMixin
from user.models import FKeyUserMixin
from others.models import FKeyJobCateroryMixin


class AbstractJob(FKeyJobCateroryMixin):
    publish_time = models.DateField(
        '发布时间',
        auto_now=True,
        help_text='发布时间',
    )
    position = models.CharField(
        '岗位',
        max_length=10,
        help_text='岗位',
    )
    pay = models.CharField(
        '薪资待遇',
        max_length=20,
        help_text='薪资待遇',
    )
    descriptions = models.CharField(
        '工作描述',
        max_length=200,
        help_text='工作描述',
    )
    requirements = models.CharField(
        '岗位要求',
        max_length=200,
        help_text='岗位要求',
    )
    benefits = models.CharField(
        '福利',
        max_length=100,
        default = '',
        blank = True,
        help_text='福利',
    )

    class Meta:
        abstract = True


class FullTimeJob(FKeyPartyAMixin, AbstractJob):
    """企业全职工作
    """

    @classproperty
    def fkey(self):
        return 'party_a'

    class Meta:
        verbose_name = '企业全职工作'
        verbose_name_plural = verbose_name


class PartTimeJob(FKeyPartyAMixin, AbstractJob):
    """企业兼职工作
    """

    @classproperty
    def fkey(self):
        return 'party_a'

    class Meta:
        verbose_name = '企业兼职工作'
        verbose_name_plural = verbose_name


class PersonalJob(FKeyUserMixin, AbstractJob):
    """个人工作
    """

    @classproperty
    def fkey(self):
        return 'user'

    class Meta:
        verbose_name = '个人工作'
        verbose_name_plural = verbose_name
