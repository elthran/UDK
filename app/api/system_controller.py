from flask import jsonify
from flask_login import current_user

from app.serializers.county_serializer import CountySerializer
from app.serializers.kingdom_serializer import KingdomSerializer
from app.serializers.user_serializer import UserSerializer


def get_current_user():
    if current_user.is_authenticated:
        return jsonify(user=UserSerializer.call(current_user))

    # Temporary code due to Vue breaking sessions
    return jsonify(user=dict(username="AnonymousUserMixin"))


def get_current_county():
    if current_user.is_authenticated:
        county = current_user.county

        return jsonify(county=CountySerializer.call(county))
    return jsonify(error="No user logged in.")


def get_current_kingdom():
    if current_user.is_authenticated:
        kingdom = current_user.county.kingdom

        return jsonify(kingdom=KingdomSerializer.call(kingdom))
    return jsonify(error="No user logged in.")
