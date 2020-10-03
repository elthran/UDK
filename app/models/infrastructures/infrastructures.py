from sqlalchemy.orm import relationship

from app.models.templates import db, GameState
from app.models.infrastructures.buildings import Building


class Infrastructure(GameState):
    county_id = db.Column(db.Integer, db.ForeignKey('county.id'), nullable=False)
    county = relationship("County", back_populates="infrastructure")

    buildings = relationship("Building", back_populates="infrastructure")

    def __init__(self, county_id, race):
        self.county_id = county_id

        self.buildings.append(Building(building_type="House", race=race))
        self.buildings.append(Building(building_type="Field", race=race))
        self.buildings.append(Building(building_type="Pasture", race=race))

        # self.house = Building(building_type="House", race=race)
        # self.field = Building(building_type="Field", race=race)
        # self.pasture = Building(building_type="Pasture", race=race)

    def get_employed_workers(self):
        total = 0
        for building in self.buildings:
            total += building.worker_capacity * building.total_owned
        return total
