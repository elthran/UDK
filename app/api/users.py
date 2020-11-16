from flask import jsonify

from app.models.users import User


def get_user(id_):
    user = User.query.get(id_)
    return jsonify(
            user=dict(id=user.id,
                      username=user.username)
        )
