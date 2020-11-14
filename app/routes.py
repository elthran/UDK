from app.main import app
from app.api.authentication import login
from app.api.counties import get_county
from app.api.users import get_user
from app.api.system import get_current_user


app.add_url_rule('/api/counties/<int:id_>', 'get_county', get_county, methods=['GET'])
# TODO: make this a real login page that accepts a posted form data thing.
# api.add_url_rule('/api/session/login', 'login', login, methods=['POST'])
app.add_url_rule('/api/session/login/<string:username>', 'login', login, methods=['GET'])
app.add_url_rule('/api/system/current_user', 'get_current_user', get_current_user, methods=['GET'])
app.add_url_rule('/api/users/<int:id_>', 'get_user', get_user, methods=['GET'])
