from flask import Blueprint

maple_bp = Blueprint('maple_story', __name__)

from src.api import maple_controller