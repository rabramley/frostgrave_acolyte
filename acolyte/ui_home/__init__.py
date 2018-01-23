"""Portal for Frostgrave Utils
"""

from flask import Blueprint, render_template, redirect, url_for
from acolyte.database import db

blueprint = Blueprint('ui_home', __name__, template_folder='templates')

@blueprint.route('/', methods=['GET'])
def index():
    """The home page - does nothing at present"""

    return render_template('index.html')
