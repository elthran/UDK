from sqlalchemy.orm import relationship

from app.models.economies import Economy
from app.models.infrastructures.infrastructures import Infrastructure
from app.models.preferences import Preference
from app.models.templates import db, GameState
from app.helpers.functions import generate_weather


class County(GameState):
    # Basics
    name = db.Column(db.String(128), nullable=False)
    leader = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    day = db.Column(db.Integer)
    race = db.Column(db.String(32))
    title = db.Column(db.String(16))
    background = db.Column(db.String(32))
    # Misc
    weather = db.Column(db.String(16))

    economy = relationship("Economy", uselist=False, back_populates="county")
    infrastructure = relationship("Infrastructure", uselist=False, back_populates="county")
    preference = relationship("Preference", uselist=False, back_populates="county")

    def __init__(self, name, leader, user_id, race, title, background):
        self.name = name
        self.leader = leader
        self.user_id = user_id
        self.race = race
        self.title = title
        self.background = background
        self.day = 0

        # Misc
        self.weather = generate_weather()

        self.save()

        print(f"CREATING ECONOMY/INFRASTRUCTURE/PREFERENCE WITH COUNTY ID {self.id}")
        self.economy = Economy(county_id=self.id)
        self.infrastructure = Infrastructure(county_id=self.id)
        self.preference = Preference(county_id=self.id)

    def __repr__(self):
        return f"<County: (Name: {self.name}, ID: {self.id})>"
