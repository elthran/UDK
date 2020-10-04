from .config.initialize import initialize

app = initialize(__name__)


def import_routes():
    import app.routes.home
    import app.routes.county.home
    import app.routes.county.economy
    import app.routes.county.infrastructure


# Serve Vue app
# app = Flask(__name__, static_folder="./ui/dist", static_url_path="/")

# @app.route('/')
# def vue_app():
#     return send_from_directory("./ui/dist", "index.html")


import_routes()
