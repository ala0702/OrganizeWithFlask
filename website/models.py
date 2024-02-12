
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
    notes = db.relationship('Note')
    #is_active = db.Column(db.Boolean, default=True)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(2000))
    date = db.Column(db.DateTime(timezone = True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# . -> current package