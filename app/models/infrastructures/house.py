from app.models.infrastructures.buildings import Building


class House(Building):
    __mapper_args__ = {'polymorphic_identity': __qualname__}

    # primary_language = db.Column(db.String(50))
    def __init__(self):
        super().__init__(self.__class__.__name__)
