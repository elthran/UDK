from expects import expect, have_keys

from app.serializers.base_serializer import BaseSerializer, field, fields

class MockModel:
    def __init__(self, id_=1, username='some_user'):
        self.id = id_
        self.username = username


class MockSerializer(BaseSerializer):
    _fields = fields("id", "username")


class TestBaseSerializer:
    def test_call(self, faker):
        id_ = faker.pyint()
        username = faker.user_name()

        mock_model = MockModel(id_=id_, username=username)

        expect(MockSerializer.call(mock_model)).to(
            have_keys(id=id_, username=username)
        )
