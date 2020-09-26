from sqlalchemy.orm import relationship

from app.helpers.constants import Buildings
from app.models.templates import db, GameState


class Building(GameState):
    infrastructure_id = db.Column(db.Integer, db.ForeignKey('infrastructure.id'), nullable=False)
    infrastructure = relationship("Infrastructure", back_populates="buildings")

    generic_name = db.Column(db.String(128))
    class_name = db.Column(db.String(128))
    total_owned = db.Column(db.Integer)
    worker_capacity = db.Column(db.Integer)
    gold_cost = db.Column(db.Integer)
    wood_cost = db.Column(db.Integer)
    stone_cost = db.Column(db.Integer)
    output = db.Column(db.Integer)
    description = db.Column(db.String(128))

    building_type = db.Column('type', db.String(50))

    __mapper_args__ = {'polymorphic_on': building_type}

    def __init__(self, building_type):
        # self.infrastructure_id = infrastructure_id
        self.generate_building_by_type(building_type)

    def generate_building_by_type(self, building_type):
        if building_type == Buildings.HOUSE:
            self.generic_name = Buildings.HOUSE
            self.class_name = "Cottage"
            self.total_owned = 20
            self.worker_capacity = 0
            self.gold_cost = 65
            self.wood_cost = 20
            self.stone_cost = 0
            self.output = 5
            self.description = f"Each percent of land built as a {self.class_name} increases your birth rate."
        elif building_type == Buildings.FIELD:
            self.generic_name = Buildings.FIELD
            self.class_name = "Meadow"
            self.total_owned = 10
            self.worker_capacity = 5
            self.gold_cost = 50
            self.wood_cost = 10
            self.stone_cost = 0
            self.output = 40
            self.description = f"Each {self.class_name} provides enough grain to feed {self.output} people a day."



