#!/usr/bin/env python3

import os
from acolyte import create_app
from acolyte.database import db
from acolyte.importer import import_spells

app = create_app()

with app.app_context():
    db.create_all()
    import_spells(app, os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'spells.yaml'
    ))

if __name__ == "__main__":
    app.run()
