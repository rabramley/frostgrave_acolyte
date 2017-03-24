"""Aplication to manage Frostgrave wizards
"""
import traceback
from flask import Flask, render_template, flash, redirect, url_for
from config import BaseConfig
from acolyte.database import initialise_db
from acolyte.forms import *


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

    @app.route('/spellbook', methods=['GET', 'POST'])
    def spellbook():
        """Collect information about which forms the wizard has"""
        form = SpellBookForm()

        if form.validate_on_submit():

            flash(form.name.data, 'success')

            for s in form.spells.entries:
                flash(s.data['name'], 'success')

            return redirect(url_for('index'))

        return render_template('spellbook.html', form=form)

    return app
