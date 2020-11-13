class BaseSerializer:
    identifier = None
    fields = None


    @classmethod
    def call(cls, model):
        data = {}
        if cls.identifier is not None:
            data['id'] = getattr(model, cls.identifier)

        if cls.fields is not None:
            for field in cls.fields:
                data[field] = getattr(model, field)

        return data
