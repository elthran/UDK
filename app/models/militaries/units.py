from sqlalchemy.orm import relationship

from app.helpers.metadata import Units
from app.models.templates import db, GameState


class Unit(GameState):
    military_id = db.Column(db.Integer, db.ForeignKey('military.id'), nullable=False)
    military = relationship("Military", back_populates="units")

    class_name = db.Column(db.String(16))
    class_name_plural = db.Column(db.String(16))
    total_owned = db.Column(db.Integer)
    gold_cost = db.Column(db.Integer)
    wood_cost = db.Column(db.Integer)
    iron_cost = db.Column(db.Integer)
    upkeep = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defence = db.Column(db.Integer)
    health = db.Column(db.Integer)
    category = db.Column(db.String(16))
    armour = db.Column(db.String(16))
    description = db.Column(db.String(128))

    def __init__(self, unit_type, race):
        self.generic_name = unit_type
        racial_metadata = getattr(Units, race)[unit_type]
        self.class_name = racial_metadata["Singular"]
        self.class_name_plural = racial_metadata["Plural"]
        self.total_owned = 0
        self.gold_cost = racial_metadata["Gold"]
        self.wood_cost = racial_metadata["Wood"]
        self.iron_cost = racial_metadata["Iron"]
        self.upkeep = racial_metadata["Upkeep"]
        self.attack = racial_metadata["Attack"]
        self.defence = racial_metadata["Defence"]
        self.health = racial_metadata["Health"]
        self.category = racial_metadata["Category"]
        self.armour = racial_metadata["Armour"]
        self.description = racial_metadata["Description"]

    def get_available(self):
        return self.total_owned




