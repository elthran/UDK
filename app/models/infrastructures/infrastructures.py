from sqlalchemy.orm import relationship

from app.helpers.constants import Buildings
from app.models.infrastructures.buildings import Building
from app.models.templates import db, GameState


class Infrastructure(GameState):
    county_id = db.Column(db.Integer, db.ForeignKey('county.id'), nullable=False)
    county = relationship("County", back_populates="infrastructure")

    buildings = relationship("Building", back_populates="infrastructure")

    def __init__(self, county_id):
        self.county_id = county_id

        self.save()

        print(f"CREATED BUILDINGS WITH INFRASTRUCTURE ID {self.id}")
        self.house = Building(infrastructure_id=self.id, infrastructure_type=Buildings.HOUSE)
        self.house.save()
        self.field = Building(infrastructure_id=self.id, infrastructure_type=Buildings.FIELD)
        self.field.save()


