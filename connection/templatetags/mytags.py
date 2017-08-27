from django import template
from connection.models import Post, Connection

register = template.Library()


@register.simple_tag
def non_public_posts():
    return Post.objects.filter(status__iexact='PUBLISHED', public=False, list=True)


@register.simple_tag(takes_context=True)
def user_conn_list(context):
    user = context['user']
    return Connection.objects.filter(user=user)


@register.filter
def link_node_conn(node, conn):
    return '%s:%s@%s:%s' % (conn.method, conn.passwd, node.domain_name, conn.port)


import base64


def base64_encode(s):
    return base64.encodebytes(s.encode()).decode().strip()


@register.filter
def qrcode_str(node, conn):
    s = link_node_conn(node, conn)
    if 'shadowsocks' in str(conn.protocol).lower():
        return 'ss://%s' % base64_encode(s)
    else:
        return str(conn.protocol).lower() + "://" + base64_encode(s)
