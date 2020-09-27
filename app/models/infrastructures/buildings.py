from sqlalchemy.orm import relationship

from app.helpers.metadata import Buildings
from app.models.templates import db, GameState


class Building(GameState):
    infrastructure_id = db.Column(db.Integer, db.ForeignKey('infrastructure.id'), nullable=False)
    infrastructure = relationship("Infrastructure", back_populates="buildings")

    building_type = db.Column(db.String(128))
    class_name = db.Column(db.String(128))
    total_owned = db.Column(db.Integer)
    worker_capacity = db.Column(db.Integer)
    gold_cost = db.Column(db.Integer)
    wood_cost = db.Column(db.Integer)
    stone_cost = db.Column(db.Integer)
    output = db.Column(db.Integer)
    description = db.Column(db.String(128))

    def __init__(self, building_type, race):
        self.generic_name = building_type
        racial_metadata = getattr(Buildings, race)[building_type]
        self.class_name = racial_metadata["Singular"]
        self.class_name_plural = racial_metadata["Plural"]
        self.total_owned = 10
        self.worker_capacity = 5
        self.gold_cost = racial_metadata["Gold"]
        self.wood_cost = racial_metadata["Wood"]
        self.stone_cost = racial_metadata["Stone"]
        self.output = racial_metadata["Output"]
        self.description = racial_metadata["Description"].format(self.output)



