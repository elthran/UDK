from flask import jsonify

from .config.initialize import initialize

app = initialize(__name__)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


def import_routes():
    import app.api.routes
    import app.routes.home
    import app.routes.county.home
    import app.routes.county.economy
    import app.routes.county.infrastructure


import_routes()
