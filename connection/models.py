# re-use models from: https://github.com/alishtory/xsadmin/blob/master/user/models.py
# design changes:
#    support multi methods on every node
#    support multi protocols
#    support config prococals & methods in admin panel

import random
from django.db.utils import ProgrammingError
from django.db.models import Max
from django.conf import settings


def gen_passwd():
    return ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 10))


def get_usefull_port():
    try:
        max_port = Connection.objects.aggregate(Max('port')).get('port__max')
    except ProgrammingError:
        max_port = None
    if not max_port:
        max_port = 4455
    new_port = int(max_port) + 1
    return new_port


from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    reg_ip = models.GenericIPAddressField(verbose_name='注册IP', unpack_ipv4=True, null=True)
    last_login_ip = models.GenericIPAddressField(verbose_name='上次登录IP', unpack_ipv4=True, null=True)
    last_login_date = models.DateTimeField(verbose_name='上次登录时间', null=True, auto_now_add=True)
    this_login_ip = models.GenericIPAddressField(verbose_name='本次登录IP', unpack_ipv4=True, null=True)
    this_login_date = models.DateTimeField(verbose_name='本次登录时间', null=True, auto_now_add=True)


class Node(models.Model):
    STATUS_CHOICES = (
        ('ON-LINE', '正常'),
        ('OFF-LINE', '离线'),
        ('BANDWIDTH-OVER', '流量用完'),
        ('ATTACKED', '被攻击中'),
        ('INIT', '初始化中'),
        ('MAINTAIN', '维护中'),
        ('OUT', '下线'),
    )

    domain_name = models.CharField(max_length=63, verbose_name='节点域名')
    location = models.CharField(max_length=127, verbose_name='节点地理位置')
    status = models.CharField(max_length=63, choices=STATUS_CHOICES, default='INIT', verbose_name='节点状态')
    traffic_rate = models.PositiveIntegerField(verbose_name='流量倍率百分比', help_text='100表示默认1倍', default=100)
    sort = models.SmallIntegerField(verbose_name='排序', default=0, help_text='小的在前面')
    remark_for_admin = models.TextField('管理员备注', null=True, blank=True, default=None)

    class Meta:
        verbose_name = '节点'
        verbose_name_plural = verbose_name
        ordering = ['sort', 'id']

    def __str__(self):
        return '%s [%s]' % (self.domain_name, self.location)


class Accessories(models.Model):
    catalog = models.CharField(verbose_name='分类', choices=settings.DB_ACCESSORIES_CATALOGS, max_length=32)
    value = models.CharField(verbose_name='值', max_length=200)

    def __str__(self):
        return '%s: %s' % (self.catalog, self.value)

    class Meta:
        verbose_name = '参数清单'
        verbose_name_plural = verbose_name
        ordering = ['-catalog']


class Connection(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1,
        verbose_name='用户'
    )

    protocol =models.ForeignKey(
        Accessories,
        limit_choices_to={'catalog': 'protocol'},
        related_name='protocols',
        default=1, # pk in /db_init.json
        on_delete=models.CASCADE,
        verbose_name="协议"
    )

    method = models.ForeignKey(
        Accessories,
        limit_choices_to={'catalog': 'method'},
        related_name='methods',
        default=100, # pk in /db_init.json
        on_delete=models.CASCADE,
        verbose_name="加密方式"
    )

    port = models.PositiveSmallIntegerField(verbose_name='端口', default=get_usefull_port)
    passwd = models.CharField(verbose_name='端口密码', max_length=16, default=gen_passwd)

    class Meta:
        verbose_name = '连接'
        verbose_name_plural = verbose_name
        ordering = ['port', 'id']

    def __str__(self):
        return '%s [%s: %s]' % (self.port, self.protocol, self.method)


from markdownx.models import MarkdownxField
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True)
    body = MarkdownxField()
    status = models.CharField('文章状态', max_length=31, choices=(('DRAFT', '草稿'), ('PUBLISHED', '已发布')), default='DRAFT')
    topped = models.BooleanField('置顶', default=False)
    public = models.BooleanField('公开', default=False)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return '%s [%s]' % (self.title, self.get_status_display())

    class Meta:
        verbose_name = '文章内容'
        verbose_name_plural = verbose_name
        ordering = ['-topped', '-last_modified_time']

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def get_slug_url(self):
        return reverse('post_detail_slug', kwargs={'slug': self.slug})
