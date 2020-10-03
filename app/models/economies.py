from sqlalchemy.orm import relationship

from app.models.templates import db, GameState


class Economy(GameState):
    county_id = db.Column(db.Integer, db.ForeignKey('county.id'), nullable=False)
    county = relationship("County", back_populates="economy")

    BASE_BUILD_SLOTS = 3
    build_slots = db.Column(db.Integer)

    BASE_HAPPINESS = 7
    happiness_change = db.Column(db.Integer)

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

    def __init__(self, county_id):
        self.county_id = county_id

        self._population = 500
        self._land = 150
        self._healthiness = 75
        self._happiness = 100
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

    def get_population_change(self):
        growth = self.get_expected_births() # + self.get_immigration_rate()
        decay = self.get_expected_deaths() # + self.get_emigration_rate()
        delta = growth - decay
        maximum_decay = -0.03 * self.population  # Can't decay more than 3% an hour
        return int(max(delta, maximum_decay))

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
        value = min(value, 10)  # Should be max_mana
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

    def get_expected_births(self):
        basic_births = (self.happiness / 100) * (self.land / 5)  # 5% times your happiness rating
        modifier = self.get_birth_rate_modifier()
        return round(basic_births * modifier)

    def get_birth_rate_modifier(self):
        house_bonus = (self.county.infrastructure.house.total_owned ** 0.75 * self.county.infrastructure.house.output) / self.land
        modifier = 1 + house_bonus
        return modifier

    def get_expected_deaths(self):
        rate = (2 / self.healthiness)
        deaths = rate * self.population
        return round(deaths)
