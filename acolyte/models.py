"""Acolyte models"""

from acolyte.database import db


class School(db.Model):
    """School SqlAlchemy model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')


class Spell(db.Model):
    """Spell SqlAlchemy model
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    required = db.Column(db.Integer)
    target = db.Column(db.String(50))
    description = db.Column(db.Text)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))

    school = db.relationship('School', backref=db.backref(
        'spells',
        order_by=name,
        cascade="all, delete-orphan"))

    def __init__(self, **kwargs):
        """Initialise model
        
        Arguments:
            **kwargs {list} -- Keyword arguments

        Keyword Arguments:
            name {str} -- Spell name
            school_id {int} -- Spell school ID
            required {int} -- Required dice roll
            target {str} -- Spell target
            description {str} -- Spell description
        """


        self.name = kwargs.get('name')
        self.school_id = kwargs.get('school_id')
        self.required = kwargs.get('required')
        self.target = kwargs.get('target')
        self.description = kwargs.get('description')
