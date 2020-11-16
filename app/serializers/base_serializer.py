def field(name, getter: None):
    assert getter is not None

    return (name, getter)


def fields(*names):
    data = []
    for name in names:
        data.append(field(name, getter=lambda model, name=name: getattr(model, name)))

    return data



class BaseSerializer:
    _fields = None

    @classmethod
    def _serialize(cls, model):
        data = {}

        if cls._fields is not None:
            for field, getter in cls._fields:
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
