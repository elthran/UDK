from .config.initialize import initialize

app = initialize(__name__)

# Super deprecate routes for UI migration
def import_routes():
    import app.routes
    import app.routes_legacy.home
    import app.routes_legacy.county.home
    import app.routes_legacy.county.economy
    import app.routes_legacy.county.infrastructure


import_routes()
