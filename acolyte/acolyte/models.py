from acolyte.database import db

aligned_table = db.Table('aligned', db.Base.metadata,
    db.Column('school_id', db.Integer, db.ForeignKey('school.id')),
    db.Column('aligned_id', db.Integer, db.ForeignKey('school.id'))
)


class School(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    aligned = db.relationship("School", secondary=aligned_table)

    opposed_id = db.Column(db.Integer, db.ForeignKey('School.id'))
    opposed = db.relationship("School")


    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')


class Spell(db.Model):

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

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.school_id = kwargs.get('school_id')
        self.required = kwargs.get('required')
        self.target = kwargs.get('target')
        self.description = kwargs.get('description')

