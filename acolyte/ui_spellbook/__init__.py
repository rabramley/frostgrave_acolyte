"""Tool to produce spellbook PDF download"""

from flask import Blueprint, render_template, redirect, url_for
from flask_weasyprint import HTML, render_pdf
from acolyte.database import db
from acolyte.forms import SpellForm, SpellBookForm
from acolyte.models import Spell

blueprint = Blueprint('ui_spellbook', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET', 'POST'])
def spellbook():
    """Display and accept form for the user to select required spells
    
    Decorators:
        blueprint
    
    Returns:
        obj -- HTML form response or redirect to PDF creation
    """


    spells_knowledges = [{
        'spell_id': sp.id,
        'school_name': sp.school.name,
        'spell_name': sp.name,
        'learnt': False} for i, sp in enumerate(Spell.query.all())]

    form = SpellBookForm(spells_knowledges=spells_knowledges)

    if form.validate_on_submit():

        spell_ids = [s.data['spell_id']
            for s in form.spells_knowledges.entries if s.data['learnt']]

        return redirect(url_for('ui_spellbook.spellbook_pdf', spell_ids=spell_ids))

    return render_template('spellbook.html', form=form)

@blueprint.route('/pdf/<list:spell_ids>')
def spellbook_pdf(spell_ids):
    """Produce spellbook PDF from list of spell IDs
    
    Decorators:
        blueprint
    
    Arguments:
        spell_ids {list} -- List of Spell IDs
    
    Returns:
        obj -- PDF response
    """


    spells = Spell.query.filter(Spell.id.in_(spell_ids)).all()

    html = render_template('spellbook_pdf.html', spells=spells)
    return render_pdf(HTML(string=html))
