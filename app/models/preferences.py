from sqlalchemy.orm import relationship

from app.helpers.constants import Rations, ProductionChoice
from app.models.templates import db, GameState


class Preference(GameState):
    county_id = db.Column(db.Integer, db.ForeignKey('county.id'), nullable=False)
    county = relationship("County", back_populates="preference")

    _tax_rate = db.Column(db.Integer)
    rations = db.Column(db.Float)
    production_choice = db.Column(db.String(16))

    def __init__(self, county_id):
        self.county_id = county_id

        self._tax_rate = 7
        self.rations = Rations.NORMAL
        self.production_choice = ProductionChoice.OVERWORK

