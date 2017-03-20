import yaml
from acolyte.models import Spell
from acolyte.database import db

def import_spell_data(app, spell_path):
    app.logger.info('Importing spells from {}'.format(spell_path))
    with open(spell_path, "r") as f:
        spells = yaml.load_all(f)

        for s in spells:

            sp = Spell.query.filter(Spell.name == s['name'].title()).first()

            if not sp:
                app.logger.info('Creating Spell: {}'.format(s['name'].title()))

                sp = Spell(
                    name=s['name'].title(),
                    school=s['school'],
                    required=s['required'],
                    target=s['target'],
                    description=s['description']
                )

            db.session.add(sp)
            db.session.commit()

    app.logger.info('Importing spells completed')
