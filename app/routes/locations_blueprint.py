from flask import Blueprint
from app.controllers.locations_controller import create_location, delete_location


bp = Blueprint('location_bp', __name__, url_prefix='/locations')

bp.post("")(create_location)
bp.delete("<int:location_id>")(delete_location)