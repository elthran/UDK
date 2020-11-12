from app.api.base import api

from app.main import app
from app.api.counties import get_county
from app.api.users import get_user
from app.api.preference import get_preference
from app.api.infrastructure import get_infrastructure

from app.api.debug import advance_day


api.add_url_rule('/counties/<int:id>', 'get_county', get_county, methods=['GET'])
api.add_url_rule('/users/<int:id>', 'get_user', get_user, methods=['GET'])
api.add_url_rule('/counties/<int:county_id>/preference', 'get_preference', get_preference, methods=['GET'])
api.add_url_rule('/counties/<int:county_id>/infrastructure', 'get_infrastructure', get_infrastructure, methods=['GET'])

api.add_url_rule('/debug/advance_day', 'advance_day', advance_day, methods=['GET'])

app.register_blueprint(api, url_prefix='/api')
