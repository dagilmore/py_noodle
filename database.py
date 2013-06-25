__author__ = 'dagilmore'

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Find heroku database; if local, default to sqlite
SQLALCHEMY_DATABASE_URI = os.environ.get(
    'DATABASE_URL', 'sqlite:////tmp/test.db'
)

engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True, echo=True,)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == 'main':
    init_db()