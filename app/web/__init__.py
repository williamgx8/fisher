from flask import Blueprint

web = Blueprint('web', __name__)

from . import book_routes
from . import user_routes
