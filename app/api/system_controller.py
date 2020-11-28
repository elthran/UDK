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


def get_current_county():
    # TODO: Make this work and use the CountySerializer that you make
    if current_user.is_authenticated:
        return jsonify(error="Not implemented.")
    return jsonify(error="No user logged in.")


def get_current_kingdom():
    if current_user.is_authenticated:
        kingdom = current_user.county.kingdom

        kingdom = dict(
            id=kingdom.id,
            name=kingdom.name,
            counties=[
                dict(
                    id=county.id,
                    name=county.name,
                    leader=county.leader,
                    land=county.economy.land,
                ) for county in kingdom.counties],
        )
        return jsonify(
            kingdom=kingdom
        )
    return jsonify(error="No user logged in.")