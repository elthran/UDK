from flask import render_template, jsonify

from app.main import app
from app.models.counties import County
from app.models.users import User
from app.serializers.county_serializer import CountySerializer


@app.route('/api/county/<int:county_id>', methods=['GET'])
def county_home(county_id):
    # user = current_user
    user = User.query.get(1)
    county = County.query.get(county_id)
    return jsonify(CountySerializer.render(county))
