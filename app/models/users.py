from app.models.templates import db, GameState


class User(GameState):
    # Basic data
    username = db.Column(db.String(128), nullable=False)

    # Flask
    is_authenticated = db.Column(db.Boolean)  # User has logged in through flask. (Flask)
    is_active = db.Column(db.Boolean)  # Account has been activated via email and not been locked. (Flask)
    is_anonymous = db.Column(db.Boolean)  # Current_user is set to is_anonymous when not yet logged in. (Flask)
    is_admin = db.Column(db.Boolean)  # Current user is a game creator with unlimited power
    is_bot = db.Column(db.Boolean)  # Current user is a game creator with unlimited power

    county = db.relationship('County', back_populates='user', uselist=False)


    def __init__(self, username):
        # Basic data
        self.username = username

        # Flask login
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False

    def get_id(self):
        # Required for flask-login
        return self.id
