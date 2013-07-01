__author__ = 'dagilmore'

import datetime

import sqlalchemy as db
from database import Base


class Post(Base):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), unique=True)
    slug = db.Column(db.String(50), unique=True)
    category = db.Column(db.String(50))
    body = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(
            self,
            title=None,
            slug=None,
            category=None,
            body=None,):

        self.title = title
        self.slug = slug
        self.category = category
        self.body = body

    def __repr__(self):
        return '<Blog %r>' % (self.title)