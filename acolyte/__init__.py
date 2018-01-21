"""Aplication to manage Frostgrave wizards
"""
import traceback
from flask import Flask, render_template
from config import BaseConfig
from acolyte.utils import ListConverter
from flask_migrate import Migrate
from acolyte.database import db
from .ui_home import blueprint as ui_home_blueprint
from .ui_spellbook import blueprint as ui_spellbook_blueprint


def create_app(config=BaseConfig):
    """ Used to create flask application"""
    app = Flask(__name__)
    app.config.from_object(config)
    app.config.from_pyfile('application.cfg', silent=True)

    with app.app_context():
        db.init_app(app)
        Migrate(app, db)

    app.url_map.converters['list'] = ListConverter

    app.register_blueprint(ui_home_blueprint)
    app.register_blueprint(ui_spellbook_blueprint, url_prefix='/spellbook')

    @app.errorhandler(500)
    @app.errorhandler(Exception)
    def internal_error(exception):
        """Catch internal exceptions and 500 errors, display
            a nice error page and log the error.
        """
        print(traceback.format_exc())
        app.logger.error(traceback.format_exc())
        return render_template('500.html'), 500

    return app
