from rest_framework import serializers
from connection.models import Connection

class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(source="passwd")
    class Meta:
        model = Connection
        fields = ( 'method', 'port', 'password')