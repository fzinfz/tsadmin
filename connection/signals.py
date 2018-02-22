from connection.models import Connection,Node
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests, sys

@receiver(post_save, sender=Connection)
def conn_save(sender, instance, created, **kwargs):
    print(sender, end=" changed: ")
    print(instance)
    for node in Node.objects.all():
        try:
            rs = requests.get(node.webhook)
            print(node.webhook + " response: ", rs.content)
        except:
            print("error: ", sys.exc_info()[0])
