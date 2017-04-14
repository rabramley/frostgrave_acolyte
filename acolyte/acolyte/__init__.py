"""Aplication to manage Frostgrave wizards
"""
import traceback
from flask import Flask, render_template, flash, redirect, url_for
from config import BaseConfig
from acolyte.database import initialise_db
from acolyte.forms import *
from acolyte.models import *
from acolyte.utils import ListConverter


def create_app(config=BaseConfig):
    """ Used to create flask application"""
    app = Flask(__name__)
    app.config.from_object(config)
    app.config.from_pyfile('application.cfg', silent=True)

    with app.app_context():
        initialise_db(app)

    app.url_map.converters['list'] = ListConverter

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

        spells_knowledges = [{
            'spell_id': sp.id,
            'school_name': sp.school.name,
            'spell_name': sp.name,
            'learnt': False} for i, sp in enumerate(Spell.query.all())]

        form = SpellBookForm(spells_knowledges=spells_knowledges)

        if form.validate_on_submit():

            spell_ids = [s.data['spell_id']
                         for s in form.spells_knowledges.entries if s.data['learnt']]

            return redirect(url_for('spellbook_pdf', spell_ids=spell_ids))

        return render_template('spellbook.html', form=form)

    @app.route('/spellbook_pdf/<list:spell_ids>')
    def spellbook_pdf(spell_ids):
        """Create a PDF based on the spells the wixard has"""

        spells = Spell.query.filter(Spell.id.in_(spell_ids)).all()

        return render_template('spellbook_pdf.html', spells=spells)

    return app
