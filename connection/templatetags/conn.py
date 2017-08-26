from django import template
from connection.models import Connection
import base64
from django.template import RequestContext

register = template.Library()

# TODO: multi ports for every user
def conn_first(uid):
    return Connection.objects.filter(user_id=uid)[0]


@register.filter
def get_protocol(node, uid):
    conn = conn_first(uid)
    return '%s:%s@%s:%s' % (conn.method, conn.passwd, node.domain_name, conn.port)


@register.filter
def ss_qrcode(node, uid):
    return 'ss://%s' % (base64.encodebytes(get_protocol(node, uid).encode()).decode().strip(),)
