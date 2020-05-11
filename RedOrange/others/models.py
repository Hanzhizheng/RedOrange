from django.db import models


class CodeNameMixin(models.Model):
    code = models.IntegerField(
        '编码',
        primary_key=True,
        help_text='编码',
    )
    name = models.CharField(
        '名称',
        max_length=25,
        help_text='名称',
    )
    
    def __str__(self):
        return self.name

    class Meta:
        abstract=True


class Province(CodeNameMixin):
    """省份
    """

    class Meta:
        verbose_name = '省份'
        verbose_name_plural = verbose_name


class City(CodeNameMixin):
    """城市
    """
    province = models.ForeignKey(
        Province,
        verbose_name='省份',
        on_delete=models.CASCADE,
        help_text='省份',
    )

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name


class Area(CodeNameMixin):
    """区县
    """
    city = models.ForeignKey(
        City,
        verbose_name='城市',
        on_delete=models.CASCADE,
        help_text='城市',
    )
    
    class Meta:
        verbose_name = '区县'
        verbose_name_plural = verbose_name


class JobCategory(CodeNameMixin):
    """岗位一级分类
    """

    class Meta:
        verbose_name = '岗位一级分类'
        verbose_name_plural = verbose_name


class JobSubCategory(CodeNameMixin):
    """岗位二级分类
    """
    category = models.ForeignKey(
        JobCategory,
        verbose_name='岗位一级分类',
        on_delete=models.CASCADE,
        help_text='岗位一级分类',
    )

    class Meta:
        verbose_name = '岗位二级分类'
        verbose_name_plural = verbose_name


class FKeyJobCateroryMixin(models.Model):
    category = models.ForeignKey(
        JobCategory,
        verbose_name='岗位一级分类',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='岗位一级分类',
    )
    sub_category = models.ForeignKey(
        JobSubCategory,
        verbose_name='岗位二级分类',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text='岗位二级分类',
    )
    class Meta:
        abstract = True