from acolyte.database import db


class School(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')


class Spell(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    school = db.Column(db.String(100))
    required = db.Column(db.Integer)
    target = db.Column(db.String(50))
    description = db.Column(db.Text)

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.school = kwargs.get('school')
        self.required = kwargs.get('required')
        self.target = kwargs.get('target')
        self.description = kwargs.get('description')
