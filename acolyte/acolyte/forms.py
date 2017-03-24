from flask_wtf import FlaskForm
from wtforms import Form, StringField, BooleanField
from wtforms.validators import DataRequired, Length
from wtforms.fields import FormField, FieldList


class SpellForm(Form):
    name = BooleanField('Name')


class SpellBookForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    spells = FieldList(FormField(SpellForm), min_entries=2)
