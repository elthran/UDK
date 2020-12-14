from flask import jsonify
from flask_login import current_user

from app.models.counties import County
from app.serializers.county_serializer import CountySerializer


def get_county(id_):
    county = County.query.get(id_)
    if county.id == current_user.county.id:
        return jsonify(county=CountySerializer.call(county, view="full_view"))

    return jsonify(county=CountySerializer.call(county))
