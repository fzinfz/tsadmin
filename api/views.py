from rest_framework import viewsets
from .serializers import *
from rest_framework import filters


class AccessoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer


class ConnectionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Returns a list of all connections.

    Remember to **filter** protocol!

    Examples:

    GET [/api/connection/?protocol=1](/api/connection/?protocol=1)

    GET [/api/connection/?protocol=1&format=json](/api/connection/?protocol=1&format=json)
    """
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer

    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('protocol',)
