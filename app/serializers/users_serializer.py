from app.serializers.base_serializer import BaseSerializer, fields


class UsersSerializer(BaseSerializer):
    _fields = fields("id", "username")
