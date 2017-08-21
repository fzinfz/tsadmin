from django.db import models
from django.db.models import Max
import random
from django.db.utils import ProgrammingError

 # re-use models from: https://github.com/alishtory/xsadmin/blob/master/user/models.py
 # main changes:
 #    support multi methods on every node
 #    support multi protocal

class Node(models.Model):
    STATUS_CHOICES = (
        ('ON-LINE','正常'),
        ('OFF-LINE','离线'),
        ('BANDWIDTH-OVER','流量用完'),
        ('ATTACKED','被攻击中'),
        ('INIT','初始化中'),
        ('MAINTAIN','维护中'),
        ('OUT','下线'),
    )

    domain_name = models.CharField(max_length=63,verbose_name='节点域名')
    location = models.CharField(max_length=127, verbose_name='节点地理位置')
    status = models.CharField(max_length=63, choices=STATUS_CHOICES,default='INIT', verbose_name='节点状态')
    traffic_rate = models.PositiveIntegerField(verbose_name='流量倍率百分比',help_text='100表示默认1倍', default=100)
    sort = models.SmallIntegerField(verbose_name='排序', default=0, help_text='小的在前面')
    remark_for_admin = models.TextField('管理员备注',null=True, blank=True, default=None)

    class Meta:
        verbose_name = '节点'
        verbose_name_plural = verbose_name
        ordering = ['sort', 'id']

    def __str__(self):
        return '%s [%s]'%(self.domain_name,self.location)


class Connection(models.Model):
    PROTOCOLS = (
        ('ss', 'Shadowsocks'),
        ('ssr', 'ShadowsocksR'),
        ('v2ray', 'V2Ray'),
    )
    protocol = models.CharField(choices=PROTOCOLS, max_length=63, default='ss', verbose_name='协议')

    METHOD_CHOICES = (
        ('rc4-md5', 'rc4-md5'),
        ('chacha20', 'chacha20'),
        ('aes-256-cfb', 'aes-256-cfb'),
        ('aes-192-cfb', 'aes-192-cfb'),
        ('aes-128-cfb', 'aes-128-cfb'),
        ('salsa20', 'salsa20'),
        ('rc4', 'rc4'),
        ('table', 'table'),
    )
    method = models.CharField(choices=METHOD_CHOICES,max_length=63, default='aes-256-cfb', verbose_name='加密方式')

    def get_usefull_port():
        try:
            max_port = Connection   .objects.aggregate(Max('port')).get('port__max')
        except ProgrammingError:
            max_port = None
        if not max_port:
            max_port = 4466
        new_port = int(max_port) + 1
        return new_port

    port = models.PositiveSmallIntegerField(verbose_name='端口', blank=True, default=get_usefull_port)

    def gen_passwd():
        return ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',10))
    passwd = models.CharField(verbose_name='端口密码',max_length=16,default=gen_passwd)

    class Meta:
        verbose_name = '连接'
        verbose_name_plural = verbose_name
        ordering = ['port', 'id']

    def __str__(self):
        return '%s [%s]'%(self.port,self.method)

