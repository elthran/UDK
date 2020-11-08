from .config.initialize import initialize
from flask import jsonify
from flask_cors import CORS

app = initialize(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


def import_routes():
    import app.routes.home
    import app.routes.county.home
    import app.routes.county.economy
    import app.routes.county.infrastructure


import_routes()
