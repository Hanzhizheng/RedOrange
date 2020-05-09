from django.db import models


def upload_to(instance, filename):
    name = instance.__class__.__name__ + 's'
    id = instance.party_a.id
    temp = (name, str(id), filename)
    return '/'.join(temp)


class PartyA(models.Model):
    """甲方
    """
    name = models.CharField(
        '名称',
        max_length=40,
        default='',
        blank=True,
        help_text='名称',
    )
    contact_number = models.CharField(
        '联系电话',
        max_length=11,
        default='',
        blank=True,
        help_text='联系电话',
    )
    address = models.CharField(
        '地址',
        max_length=50,
        default='',
        blank=True,
        help_text='地址',
    )
    license = models.ImageField(
        '营业执照',
        upload_to='Licences/',
        help_text='营业执照',
    )
    id_cards = models.ImageField(
        '经营者/法人身份证件',
        upload_to='IDCards/',
        help_text='经营者/法人身份证件',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '甲方'
        verbose_name_plural = verbose_name


class FKeyPartyAMixin(models.Model):
    party_a = models.ForeignKey(
        PartyA,
        verbose_name='甲方',
        on_delete=models.CASCADE,
        help_text='甲方',
    )

    class Meta:
        abstract = True


class PhotoAlbum(FKeyPartyAMixin):
    """甲方图片
    """
    img = models.ImageField(
        '展示图片',
        upload_to=upload_to,
        help_text='展示图片',
    )

    class Meta:
        verbose_name = '甲方图片'
        verbose_name_plural = verbose_name


class Campaign(FKeyPartyAMixin):
    """宣传活动
    """
    title = models.CharField(
        '标语',
        max_length=30,
        help_text='标语',
    )
    img = models.ImageField(
        '宣传图片',
        upload_to=upload_to,
        default='',
        blank=True,
        help_text='宣传图片',
    )
    content = models.TextField(
        '活动内容',
        default='',
        blank=True,
        help_text='活动内容',
    )
    start_date = models.DateField(
        '开始日期',
        help_text='开始日期',
    )
    stop_date = models.DateField(
        '结束日期',
        help_text='结束日期',
    )

    class Meta:
        verbose_name = '宣传活动'
        verbose_name_plural = verbose_name