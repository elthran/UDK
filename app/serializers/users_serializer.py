from app.serializers.base_serializer import BaseSerializer


class UsersSerializer(BaseSerializer):
    identifier = "id"

    fields = ["username"]
