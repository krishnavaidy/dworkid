from flask_login import UserMixin
from flask_mongoengine import MongoEngine, Document
from views import db

class User(UserMixin, db.Document):
    meta = {'collection': 'dworkid'}
    email = db.StringField(max_length=30)
    publicAddress = db.StringField(max_length=30)
    type_user = db.StringField(max_length=10)
    password = db.StringField()
