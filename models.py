from datetime import datetime

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author')

    def __str__(self):
        return '<User {}>'.format(self.username)

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(50))
    text = db.Column(db.String(1000))
    dt_create = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __str__(self):
        return '<User {}>'.format(self.username)

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'id': self.id,
            'header': self.header,
            'text': self.text,
            'dt_create': self.dt_create,
            'id_user': self.id_user
        }
