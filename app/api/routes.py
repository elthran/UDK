from app.api.base import api

from app.main import app
from app.api.counties import get_county
from app.api.users import get_user


api.add_url_rule('/counties/<int:id_>', 'get_county', get_county, methods=['GET'])
api.add_url_rule('/users/<int:id_>', 'get_user', get_user, methods=['GET'])

app.register_blueprint(api, url_prefix='/api')
