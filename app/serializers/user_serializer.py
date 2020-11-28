from app.serializers.base_serializer import BaseSerializer, fields


class UserSerializer(BaseSerializer):
    def __init__(self, user):
        super().__init__(user)
        self.fields("id", "username", county_id=user.county.id)
