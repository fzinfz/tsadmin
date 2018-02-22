from connection.models import Connection,Node
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
import requests, sys

@receiver(post_delete, sender=Connection)
@receiver(post_save, sender=Connection)
def conn_save(sender,  **kwargs):
    print(sender, end=" changed: ")
    print(kwargs)
    for node in Node.objects.all():
        try:
            rs = requests.get(node.webhook)
            print(">>> " + node.webhook + " response: ", rs.content)
        except:
            print("error: ", sys.exc_info()[0])
