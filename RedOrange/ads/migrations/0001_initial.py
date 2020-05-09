# Generated by Django 3.0.6 on 2020-05-08 01:54

import ads.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartyA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', help_text='名称', max_length=40, verbose_name='名称')),
                ('contact_number', models.CharField(blank=True, default='', help_text='联系电话', max_length=11, verbose_name='联系电话')),
                ('address', models.CharField(blank=True, default='', help_text='地址', max_length=50, verbose_name='地址')),
                ('license', models.ImageField(help_text='营业执照', upload_to='Licences/', verbose_name='营业执照')),
                ('id_cards', models.ImageField(help_text='经营者/法人身份证件', upload_to='IDCards/', verbose_name='经营者/法人身份证件')),
            ],
            options={
                'verbose_name': '甲方',
                'verbose_name_plural': '甲方',
            },
        ),
        migrations.CreateModel(
            name='PhotoAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(help_text='展示图片', upload_to=ads.models.upload_to, verbose_name='展示图片')),
                ('party_a', models.ForeignKey(help_text='甲方', on_delete=django.db.models.deletion.CASCADE, to='ads.PartyA', verbose_name='甲方')),
            ],
            options={
                'verbose_name': '甲方图片',
                'verbose_name_plural': '甲方图片',
            },
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='标语', max_length=30, verbose_name='标语')),
                ('img', models.ImageField(blank=True, default='', help_text='宣传图片', upload_to=ads.models.upload_to, verbose_name='宣传图片')),
                ('content', models.TextField(blank=True, default='', help_text='活动内容', verbose_name='活动内容')),
                ('start_date', models.DateField(help_text='开始日期', verbose_name='开始日期')),
                ('stop_date', models.DateField(help_text='结束日期', verbose_name='结束日期')),
                ('party_a', models.ForeignKey(help_text='甲方', on_delete=django.db.models.deletion.CASCADE, to='ads.PartyA', verbose_name='甲方')),
            ],
            options={
                'verbose_name': '宣传活动',
                'verbose_name_plural': '宣传活动',
            },
        ),
    ]
