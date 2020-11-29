from app.serializers.base_serializer import BaseSerializer, fields


class UserSerializer(BaseSerializer):
    _fields = fields("id", "username")
