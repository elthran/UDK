import re


def camel_case(string):
    """Convert a string to camelCase.

    Args:
        string - string to be converted to camel case.

    Examples:
        camel_case("Hello World") == "helloWorld"
        camel_case("Hello,world") == "hello,World"
        camel_case("Hello_world") == "helloWorld"
        camel_case("hello_world.txt_includehelp-WEBSITE") == \
            "helloWorld.TxtIncludehelpWebsite"
    """
    string = re.sub(r"(_|-)+", " ", string).title().replace(" ", "")
    return string[0].lower() + string[1:]
