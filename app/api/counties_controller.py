from flask import jsonify

from app.models.counties import County
from app.serializers.county_serializer import CountySerializer


def get_county(id_):
    county = County.query.get(id_)

    return jsonify(county=CountySerializer.call(county, view="full_view"))
