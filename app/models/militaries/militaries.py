from sqlalchemy.orm import relationship

from app.models.templates import db, GameState
from app.models.militaries.units import Unit


class Military(GameState):
    county_id = db.Column(db.Integer, db.ForeignKey('county.id'), nullable=False)
    county = relationship("County", back_populates="military")

    units = relationship("Unit", back_populates="military")

    def __init__(self, county_id, race):
        self.county_id = county_id

        self.peasant = Unit(unit_type="Peasant", race=race)
        self.soldier = Unit(unit_type="Soldier", race=race)
        self.archer = Unit(unit_type="Archer", race=race)

        self.units = [self.peasant, self.soldier, self.archer]

    def offensive_power(self):
        power = 0
        for unit in self.units:
            power += unit.get_available() * unit.attack
        return power

    def defensive_power(self):
        power = 0
        for unit in self.units:
            power += unit.get_available() * unit.defence
        return power
