from app.api.base import api

from app.main import app
from app.api.authentication import login
from app.api.counties import get_county
from app.api.users import get_user
from app.api.system import get_current_user


api.add_url_rule('/counties/<int:id_>', 'get_county', get_county, methods=['GET'])
# TODO: make this a real login page that accepts a posted form data thing.
# api.add_url_rule('/session/login', 'login', login, methods=['POST'])
api.add_url_rule('/session/login/<string:username>', 'login', login, methods=['GET'])
api.add_url_rule('/system/current_user', 'get_current_user', get_current_user, methods=['GET'])
api.add_url_rule('/users/<int:id_>', 'get_user', get_user, methods=['GET'])

app.register_blueprint(api, url_prefix='/api')
