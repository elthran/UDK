from flask import jsonify
from flask_login import current_user


def get_current_user():
    if current_user.is_authenticated:
        return jsonify(
            user=dict(id=current_user.id,
                      username=current_user.username,
                      countyId=current_user.county.id)
        )

       # Temporary code due to Vue breaking sessions
    return jsonify(
        user=dict(username="AnonymousUserMixin")
    )
