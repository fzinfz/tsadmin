# Execute:
# ./manage.py shell < ./scripts/init_data_method.shell.py

from django.core.exceptions import ObjectDoesNotExist
from connection.models import Accessories
from connection.utils import get_method_list

# from output of `ssserver -h`
s = """
     Sodium:
        chacha20-poly1305, chacha20-ietf-poly1305,
        xchacha20-ietf-poly1305,
        sodium:aes-256-gcm,
        salsa20, chacha20, chacha20-ietf.
     Sodium 1.0.12:
        xchacha20
     OpenSSL:
        aes-{128|192|256}-gcm, aes-{128|192|256}-cfb,
        aes-{128|192|256}-ofb, aes-{128|192|256}-ctr,
        camellia-{128|192|256}-cfb,
        bf-cfb, cast5-cfb, des-cfb, idea-cfb,
        rc2-cfb, seed-cfb,
        rc4, rc4-md5, table.
     OpenSSL 1.1:
        aes-{128|192|256}-ocb
     mbedTLS:
        mbedtls:aes-{128|192|256}-cfb128,
        mbedtls:aes-{128|192|256}-ctr,
        mbedtls:camellia-{128|192|256}-cfb128,
        mbedtls:aes-{128|192|256}-gcm
"""

print('updating Accessories(catalog="method")')
for item in get_method_list(s):
    try:
        Accessories.objects.get(catalog="method", value=item)
    except ObjectDoesNotExist:
        Accessories.objects.create(catalog="method", value=item)
        print("New item added: " + item)
