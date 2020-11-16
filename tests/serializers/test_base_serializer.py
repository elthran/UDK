from expects import expect, have_keys

from app.serializers.base_serializer import BaseSerializer, field, fields

class MockModel:
    def __init__(self, id_=None, username=None, first_name=None, last_name=None):
        self.id = id_
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class TestBaseSerializer:
    def test_call(self, faker):
        class MockSerializer(BaseSerializer):
            _fields = fields("id", "username")

        id_ = faker.pyint()
        username = faker.user_name()

        mock_model = MockModel(id_=id_, username=username)

        expect(MockSerializer.call(mock_model)).to(have_keys(id=id_, username=username))

    def test_field(self, faker):
        class MockSerializer(BaseSerializer):
            _fields = fields("id", "username")
            _fields.append(field("fullname", getter=lambda mock: mock.get_full_name()))

        id_ = faker.pyint()
        username = faker.user_name()
        first_name = faker.first_name()
        last_name = faker.last_name()

        mock_model = MockModel(
            id_=id_, username=username, first_name=first_name, last_name=last_name
        )

        expect(MockSerializer.call(mock_model)).to(
            have_keys(id=id_, username=username, fullname=f"{first_name} {last_name}")
        )
