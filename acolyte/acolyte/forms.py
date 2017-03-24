from flask_wtf import FlaskForm
from wtforms import Form, TextField, HiddenField, SelectField, StringField
from wtforms.validators import DataRequired, Length
from wtforms.fields import FormField, FieldList


class SpellForm(Form):
    name = HiddenField("Spell Name")


class SpellsForm(FlaskForm):
    wizard_school = SelectField("Wizard School",
                                validators=[DataRequired()])
    spells = FieldList(FormField(SpellForm))


class SpellBookForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
