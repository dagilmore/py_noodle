__author__ = 'dgilmore'

import datetime

from sqlalchemy import Column, Integer, String, UnicodeText, DateTime
from database import Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), unique=True)
    slug = Column(String(50), unique=True)
    category = Column(String(50), unique=True)
    body = Column(UnicodeText)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(
            self,
            title=None,
            slug=None,
            body=None):

        self.title = title
        self.slug = slug
        self.body = body

    def __repr__(self):
        return '<Post %r>' % (self.title)