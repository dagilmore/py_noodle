__author__ = 'dagilmore'

import datetime

from sqlalchemy import Column, Integer, String, UnicodeText, DateTime
from database import Base


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), unique=True)
    slug = Column(String(50), unique=True)
    category = Column(String(50))
    body = Column(UnicodeText)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

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