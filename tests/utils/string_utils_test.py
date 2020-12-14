from app.utils.string_utils import camel_case


class TestStringUtils:
    """Test the various helpfull string manipulation functions."""

    def test_camel_case(self):
        """Assert that the camel_case function converts strings to camelCase."""

        assert camel_case("Hello World") == "helloWorld"
        assert camel_case("Hello,world") == "hello,World"
        assert camel_case("Hello_world") == "helloWorld"
        assert (
            camel_case("hello_world.txt_includehelp-WEBSITE")
            == "helloWorld.TxtIncludehelpWebsite"
        )
