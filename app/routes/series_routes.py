from flask import Flask, Blueprint
from app.controllers import series_controllers

bp = Blueprint("series", __name__, url_prefix="/series")

bp.get("")(series_controllers.series)

bp.get("/<int:id>")(series_controllers.select_by_id)

bp.post("")(series_controllers.create)
