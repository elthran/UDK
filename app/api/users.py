from flask import jsonify

from app.models.users import User


def get_user(id):
    user = User.query.get(id)
    return jsonify(
        dict(id=user.id,
             username=user.username)
    )