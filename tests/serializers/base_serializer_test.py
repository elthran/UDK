from expects import expect, have_keys

from app.serializers.base_serializer import (
    BaseSerializer,
    camel_case,
)


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
            def __init__(self, model):
                super().__init__(model)
                self.fields("id", "username")

        id_ = faker.pyint()
        username = faker.user_name()

        mock_model = MockModel(id_=id_, username=username)

        expect(MockSerializer.call(mock_model)).to(have_keys(id=id_, username=username))

    def test_call_camel_case(self, faker):
        """Test that the serializer converts all field names to camel case.

        Args:
            faker: a pytest fixture for generation fake data.
        """

        class MockSerializer(BaseSerializer):
            def __init__(self, model):
                super().__init__(model)
                self.fields("first_name")

        first_name = faker.first_name()

        mock_model = MockModel(first_name=first_name)

        expect(MockSerializer.call(mock_model)).to(have_keys(firstName=first_name))

    def test_field(self, faker):
        class MockSerializer(BaseSerializer):
            def __init__(self, model):
                super().__init__(model)
                self.fields("id", "username", fullname=model.get_full_name())

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

    def test_camel_case(self):
        """Assert that the camel_case function converts strings to camelCase."""

        assert camel_case("Hello World") == "helloWorld"
        assert camel_case("Hello,world") == "hello,World"
        assert camel_case("Hello_world") == "helloWorld"
        assert (
            camel_case("hello_world.txt_includehelp-WEBSITE")
            == "helloWorld.TxtIncludehelpWebsite"
        )
