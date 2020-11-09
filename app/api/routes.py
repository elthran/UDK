from app.api.base import api

from app.main import app
from app.api.counties import get_county
from app.api.preference import get_preference
from app.api.infrastructure import get_infrastructure


api.add_url_rule('/counties/<int:id>', 'get_county', get_county, methods=['GET'])
api.add_url_rule('/counties/<int:county_id>/preference', 'get_preference', get_preference, methods=['GET'])
api.add_url_rule('/counties/<int:county_id>/infrastructure', 'get_infrastructure', get_infrastructure, methods=['GET'])

app.register_blueprint(api, url_prefix='/api')
