from app.models.templates import db, GameState


class World(GameState):
    kingdoms = db.relationship('Kingdom', backref='world')
    age = db.Column(db.Integer)
    day = db.Column(db.Integer)
    season = db.Column(db.String(16))

    def __init__(self):
        self.age = 1
        self.day = 0
        self.season = "Summer"

    def advance_day(self):
        for kingdom in self.kingdoms:
            kingdom.advance_day()
        self.day += 1

    def advance_age(self):
        pass

