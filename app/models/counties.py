from sqlalchemy.orm import relationship

from app.models.economies import Economy
from app.models.infrastructures.infrastructures import Infrastructure
from app.models.militaries.militaries import Military
from app.models.preferences import Preference
from app.models.templates import db, GameState
from app.helpers.functions import generate_weather


class County(GameState):
    # Basics
    name = db.Column(db.String(128), nullable=False)
    leader = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='county')
    kingdom_id = db.Column(db.Integer, db.ForeignKey('kingdom.id'), nullable=False)
    race = db.Column(db.String(16))
    title = db.Column(db.String(16))
    background = db.Column(db.String(16))
    # Misc
    weather = db.Column(db.String(16))

    economy = relationship("Economy", uselist=False, back_populates="county")
    infrastructure = relationship("Infrastructure", uselist=False, back_populates="county")
    military = relationship("Military", uselist=False, back_populates="county")
    preference = relationship("Preference", uselist=False, back_populates="county")

    def __init__(self, kingdom_id, name, leader, user_id, race, title, background):
        self.kingdom_id = kingdom_id
        self.name = name
        self.leader = leader
        self.user_id = user_id
        self.race = race
        self.title = title
        self.background = background

        # Misc
        self.weather = generate_weather()

        self.save()

        print(f"CREATING ECONOMY/INFRASTRUCTURE/PREFERENCE WITH COUNTY ID {self.id}")
        self.economy = Economy(county_id=self.id)
        self.infrastructure = Infrastructure(county_id=self.id, race=self.race)
        self.military = Military(county_id=self.id, race=self.race)
        self.preference = Preference(county_id=self.id)

    @property
    def day(self):
        return self.kingdom.world.day

    def advance_day(self):
        self.economy.gold += 25
        self.economy.wood += 25
        self.economy.iron += 25
        self.economy.stone += 5
