from re import sub


def field(name, getter: None):
    assert getter is not None

    return (name, getter)


def fields(*names):
    data = []
    for name in names:
        data.append(field(name, getter=lambda model, name=name: getattr(model, name)))

    return data


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
    string = sub(r"(_|-)+", " ", string).title().replace(" ", "")
    return string[0].lower() + string[1:]


class BaseSerializer:
    _key_transformer = camel_case
    _fields = None

    @classmethod
    def _serialize(cls, model):
        data = {}

        if cls._fields is not None:
            for field, getter in cls._fields:
                if cls._key_transformer is not None:
                    transformed_field = cls._key_transformer(field)
                    data[transformed_field] = getter(model)
                    continue

                data[field] = getter(model)

        return data

    @classmethod
    def call(cls, model_or_models):
        try:
            data = []
            for model in model_or_models:
                data.append(cls._serialize(model))

            return data

        except TypeError:
            return cls._serialize(model_or_models)
