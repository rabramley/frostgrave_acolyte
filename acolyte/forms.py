"""Acolyte WTF forms"""

from flask_wtf import FlaskForm
from wtforms import BooleanField, HiddenField
from wtforms.fields import FormField, FieldList


class SpellForm(FlaskForm):
    """WTF form to select a spell
    """

    spell_id = HiddenField('spell_id')
    spell_name = HiddenField('spell_name')
    learnt = BooleanField('Learnt')
    school_name = HiddenField('school_name')

class SpellBookForm(FlaskForm):
    """WTF form to select multiple spells
    """

    spells_knowledges = FieldList(FormField(SpellForm), min_entries=1)
