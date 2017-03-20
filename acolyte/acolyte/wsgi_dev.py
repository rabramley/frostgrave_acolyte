import os
from acolyte import create_app
from acolyte.database import upgrade_db
from acolyte.importer import import_spell_data

app = create_app()

with app.app_context():
    upgrade_db(app)
    import_spell_data(app, os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'spells.yaml'
    ))

