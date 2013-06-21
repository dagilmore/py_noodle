__author__ = 'dgilmore'

from sqlalchemy import Column, Integer, String, Text
from database import Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True)
    slug = Column(String(50), unique=True)
    body = Column(Text)

    def __init__(self, name=None, email=None):
        self.title = title
        self.slug = slug

    def __repr__(self):
        return '<Post %r>' % (self.title)