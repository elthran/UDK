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


class BaseSerializer:
    def __init__(self, model, view=None, key_transformer=camel_case):
        self.model = model
        self._key_transformer = key_transformer
        self._fields = {}
        self._current_view = view

        self.apply_view(view)

    def fields(self, *basic_fields, **custom_fields):
        self._fields = {}
        self.add_fields(*basic_fields, **custom_fields)

    def add_fields(self, *basic_fields, **custom_fields):
        for field in basic_fields:
            self._fields[field] = getattr(self.model, field)

        self._fields.update(custom_fields)

    def apply_view(self, view):
        if view is None:
            return

        getattr(self, view)(self.model)

    def tranform_keys(self):
        return {
            self._key_transformer(key): value for (key, value) in self._fields.items()
        }

    @classmethod
    def _serialize(cls, model, **kwargs):
        serializer = cls(model, **kwargs)

        try:
            return serializer.tranform_keys()
        except ValueError:
            return serializer._fields

    @classmethod
    def call(cls, model_or_models, **kwargs):
        try:
            return [cls._serialize(model, **kwargs) for model in model_or_models]
        except TypeError:
            return cls._serialize(model_or_models, **kwargs)
