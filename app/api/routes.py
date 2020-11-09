from app.api.base import api

from app.main import app
from .county.home import county_home


api.add_url_rule('/county/home', 'county_home', county_home, methods=['GET'])

app.register_blueprint(api, url_prefix='/api')
