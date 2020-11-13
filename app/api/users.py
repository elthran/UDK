from flask import jsonify
from flask_login import current_user

from app.models.users import User


def get_user(id_):
    # user = User.query.get(id_)
    # return jsonify(
    #         user=dict(id=user.id,
    #                   username=user.username)
    #     )

    # Temporary code due to Vue breaking sessions

    if current_user.is_authenticated:
        return jsonify(
            user=dict(id=current_user.id,
                      username=current_user.username)
        )
    return jsonify(
            user=dict(username="AnonymousUserMixin")
        )
