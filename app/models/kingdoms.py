from sqlalchemy.orm import relationship

from app.models.templates import db, GameState


class Kingdom(GameState):
    world_id = db.Column(db.Integer, db.ForeignKey('world.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    counties = db.relationship('County', backref='kingdom')

    def __init__(self, name):
        self.world_id = 1
        self.name = name

    def advance_day(self):
        for county in self.counties:
            county.advance_day()

    def __repr__(self):
        return '<Kingdom %r (%r)>' % (self.name, self.id)

