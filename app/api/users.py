from flask import jsonify
from flask_login import current_user, login_user

from app.models.users import User


def get_user(id_):
    # user = User.query.get(id_)
    # Temporary code due to Vue breaking sessions
    prebuilt_user = User.query.get(1)
    login_user(prebuilt_user)
    return jsonify(
        user=dict(id=current_user.id,
                  username=current_user.username)
    )
