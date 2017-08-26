from django import template
from connection.models import Post, Connection

register = template.Library()


@register.simple_tag
def non_public_posts():
    return Post.objects.filter(status__iexact='PUBLISHED', public=False)


@register.simple_tag(takes_context=True)
def user_conn_list(context):
    user = context['user']
    return Connection.objects.filter(user=user)


@register.filter
def get_protocol(node, conn):
    return '%s:%s@%s:%s' % (conn.method, conn.passwd, node.domain_name, conn.port)


import base64


@register.filter
def ss_qrcode(node, conn):
    return 'ss://%s' % (base64.encodebytes(get_protocol(node, conn).encode()).decode().strip(),)
