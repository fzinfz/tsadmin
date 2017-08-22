from rest_framework import serializers
from connection.models import Connection, Accessories


class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(source="passwd")

    method = serializers.SlugRelatedField(read_only=True, slug_field="value" )

    class Meta:
        model = Connection
        fields = ('method', 'port', 'password')