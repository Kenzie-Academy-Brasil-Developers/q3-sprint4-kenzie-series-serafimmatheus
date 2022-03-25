from flask import Blueprint, Flask
from .series_routes import bp as series_bp

bp_app = Blueprint("api", __name__, url_prefix="")


def init_app(app: Flask):

    bp_app.register_blueprint(series_bp)

    app.register_blueprint(bp_app)