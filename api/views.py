from rest_framework import viewsets
from connection.models import Connection, Accessories
from .serializers import *
from rest_framework import generics, filters

class ConnectionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns a list of all connections.

    Remember to **filter** protocol!

    Examples:

    GET [/api/connection/?protocol=ss](/api/connection/?protocol=ss)

    GET [/api/connection/?protocol=ss&format=json](/api/connection/?protocol=ss&format=json)
    """
    queryset = Connection.objects.all().order_by('id')
    serializer_class = ConnectionSerializer

    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('protocol',)
