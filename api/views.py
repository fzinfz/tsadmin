from rest_framework import viewsets
from .serializers import *
from rest_framework import filters


class AccessoriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer


class ConnectionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Remember to **filter** `protocol` if multi protocols used! 

    如果使用了多协议，请使用**过滤器**筛选`协议`！

    URL:

    [/api/connection/?protocol=1](/api/connection/?protocol=1)

    [/api/connection/?protocol=1&format=json](/api/connection/?protocol=1&format=json)
    """
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer

    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('protocol',)
