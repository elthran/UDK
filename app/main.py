from .config.initialize import initialize

app = initialize(__name__)


def import_routes():
    import app.routes.home


import_routes()
