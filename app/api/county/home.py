from flask import jsonify

from app.models.counties import County
from app.models.users import User


def county_home():
    # user = current_user
    user = User.query.get(1)
    county = County.query.get(1)
    return jsonify(
        user=dict(
            id=user.id,
            username=user.username,
        ),
        county=dict(
            title=county.title,
            leader=county.leader,
            race=county.race,
            background=county.background,
        )
    )
