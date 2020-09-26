from sqlalchemy.orm import relationship

from app.helpers.constants import Buildings
from app.models.infrastructures.house import House
from app.models.templates import db, GameState


class Infrastructure(GameState):
    county_id = db.Column(db.Integer, db.ForeignKey('county.id'), nullable=False)
    county = relationship("County", back_populates="infrastructure")

    buildings = relationship("Building", back_populates="infrastructure")

    house = relationship(
        "House",
        primaryjoin="and_(Infrastructure.id==Building.infrastructure_id, "
                        "Building.building_type=='House')",
        uselist=False
    )

    def __init__(self, county_id):
        self.county_id = county_id

        # self.save()

        # self.buildings.append(House())
        self.house = House()

        # self.house = Building(infrastructure_id=self.id, infrastructure_type=Buildings.HOUSE)
        # self.house.save()
        # self.field = Building(infrastructure_id=self.id, infrastructure_type=Buildings.FIELD)
        # self.field.save()
        self.save()
        print(f"CREATED BUILDINGS WITH INFRASTRUCTURE ID {self.id}")
        print('self.house.id', self.house.id)


