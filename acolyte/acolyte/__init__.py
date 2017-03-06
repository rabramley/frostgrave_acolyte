"""Aplication to manage Frostgrave wizards
"""
import traceback
from flask import Flask, render_template
from config import BaseConfig
from acolyte.database import initialise_db


def create_app(config=BaseConfig):
    """ Used to create flask application"""
    app = Flask(__name__)
    app.config.from_object(config)
    app.config.from_pyfile('application.cfg', silent=True)

    with app.app_context():
        initialise_db(app)

    @app.errorhandler(500)
    @app.errorhandler(Exception)
    def internal_error(exception):
        """Catch internal exceptions and 500 errors, display
            a nice error page and log the error.
        """
        print(traceback.format_exc())
        app.logger.error(traceback.format_exc())
        return render_template('500.html'), 500

    @app.route('/', methods=['GET'])
    def index():
        """The home page - does nothing at present"""

        return render_template('index.html')

    return app
