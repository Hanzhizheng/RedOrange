from django.db import models
from ads.models import FKeyPartyAMixin


class AbstractJob(FKeyPartyAMixin):
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


class FullTimeJob(AbstractJob):
    """全职工作
    """

    class Meta:
        verbose_name = '全职工作'
        verbose_name_plural = verbose_name


class ShortTimeJob(AbstractJob):
    """短期工作
    """

    class Meta:
        verbose_name = '短期工作'
        verbose_name_plural = verbose_name