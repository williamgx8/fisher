from flask import Blueprint

web = Blueprint('web', __name__)

from . import book_routes
from . import user_routes
from . import auth_routes
from . import drift_routes
from . import gift_routes
from . import main_routes
from . import user_routes
from . import wish_routes
