from flask_wtf import FlaskForm
from wtforms import Form, StringField, BooleanField, TextField, HiddenField
from wtforms.validators import DataRequired, Length
from wtforms.fields import FormField, FieldList


class SpellForm(FlaskForm):
    spell_id = HiddenField('spell_id')
    spell_name = HiddenField('spell_name')
    learnt = BooleanField('Learnt')
    school_name = HiddenField('school_name')

class SpellBookForm(FlaskForm):
    spells_knowledges = FieldList(FormField(SpellForm), min_entries=1)
