from app.utils.string_utils import camel_case


class BaseSerializer:
    def __init__(self, model, view=None, key_transformer=camel_case):
        self.model = model
        self.current_view = view
        self._key_transformer = key_transformer
        self._fields = {}

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
        serializer.apply_view(serializer.current_view)

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
