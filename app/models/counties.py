from app.models.templates import db, GameState


class County(GameState):
    name = db.Column(db.String(128), nullable=False)
    leader = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    day = db.Column(db.Integer)

    race = db.Column(db.String(32))
    title = db.Column(db.String(16))
    background = db.Column(db.String(32))

    _population = db.Column(db.Integer)
    _land = db.Column(db.Integer)
    _happiness = db.Column(db.Integer)  # Out of 100
    _healthiness = db.Column(db.Integer)  # Out of 100

    _gold = db.Column(db.Integer)
    _wood = db.Column(db.Integer)
    _iron = db.Column(db.Integer)
    _stone = db.Column(db.Integer)
    _research = db.Column(db.Integer)
    _mana = db.Column(db.Integer)

    grain_stores = db.Column(db.Integer)

    def __init__(self, name, leader, user_id, race, title, background):
        self.name = name
        self.leader = leader
        self.user_id = user_id
        self.race = race
        self.title = title
        self.background = background
        self.day = 0
        # Basic resources
        self._population = 500
        self._land = 150
        self._healthiness = 75
        self._happiness = 100
        # Resources
        self._gold = 750
        self._wood = 250
        self._iron = 50
        self._stone = 0
        self._research = 0
        self._mana = 0
        self.grain_stores = 500

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        self._population = max(value, 1)

    @property
    def land(self):
        return self._land

    @land.setter
    def land(self, value):
        if value <= 0:
            self._land = "YOU LOST THE GAME"
        self._land = value

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold = max(value, 0)

    @property
    def wood(self):
        return self._wood

    @wood.setter
    def wood(self, value):
        self._wood = max(value, 0)

    @property
    def iron(self):
        return self._iron

    @iron.setter
    def iron(self, value):
        self._iron = max(value, 0)

    @property
    def stone(self):
        return self._stone

    @stone.setter
    def stone(self, value):
        self._stone = max(value, 0)

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        value = min(value, self.max_mana)
        self._mana = max(value, 0)

    @property
    def happiness(self):
        return self._happiness

    @happiness.setter
    def happiness(self, value):
        self._happiness = int(max(min(100, value), 1))

    @property
    def healthiness(self):
        return self._healthiness

    @healthiness.setter
    def healthiness(self, value):
        self._healthiness = int(max(min(100, value), 1))

    def __repr__(self):
        return f"<County: (Name: {self.name}, ID: {self.id})>"
