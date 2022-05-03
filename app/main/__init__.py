from json.tool import main  # noqa: F401
from flask import Blueprint
main = Blueprint('main', __name__)
from . import views
# from . import views