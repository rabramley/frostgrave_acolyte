import yaml
from acolyte.models import Spell, School
from acolyte.database import db


def import_spells(app, spell_path):
    app.logger.info('Importing spells from {}'.format(spell_path))
    with open(spell_path, "r") as f:
        spells = yaml.load_all(f)

        for school_details in spells:

            school = School.query.filter(
                School.name == school_details['name']).first()

            if not school:
                app.logger.info('New School: {}'.format(
                    school_details['name'].title()))

                school = School(
                    name=school_details['name']
                )

                db.session.add(school)

            for spell_details in school_details['spells']:
                spell = Spell.query.filter(
                    Spell.name == spell_details['name'].title()).first()

                if not spell:
                    app.logger.info('New Spell: {}'.format(
                        spell_details['name'].title()))

                    spell = Spell(
                        name=spell_details['name'].title(),
                        school_id=school.id,
                        required=spell_details['required'],
                        target=spell_details['target'],
                        description=spell_details['description']
                    )

                db.session.add(spell)

    db.session.commit()

    app.logger.info('Importing spells completed')
