from flask_login import LoginManager

from app.models.users import User


login_manager = LoginManager()

@login_manager.user_loader
def load_user(id_):
    return User.query.get(id_)

