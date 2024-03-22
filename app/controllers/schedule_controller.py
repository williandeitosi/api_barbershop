from flask import Blueprint, jsonify
from models.model import Hour

hour_bp = Blueprint("hour_bp", __name__)


@hour_bp.route("/")
def available():
    hr = Hour.select().dicts()
    return jsonify(list(hr))
