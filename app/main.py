from .config.initialize import initialize

app = initialize(__name__)


def import_routes():
    import app.routes.home
    import app.routes.county.home
    import app.routes.county.economy
    import app.routes.county.infrastructure


import_routes()
