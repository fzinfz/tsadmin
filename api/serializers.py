from rest_framework import serializers
from connection.models import Connection, Accessories


class AccessoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accessories
        fields = '__all__'

class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(source="passwd")

    method = serializers.SlugRelatedField(read_only=True, slug_field="value" )
#    method = serializers.StringRelatedField(read_only=True, many=False)   # read __unicode__

    class Meta:
        model = Connection
        fields = ('port', 'method', 'password')
