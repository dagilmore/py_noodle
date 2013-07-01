__author__ = 'dagilmore'

from database import engine
from sqlalchemy.orm import scoped_session, sessionmaker
from py_noodle.users.models import User

# create a Session
session = scoped_session(sessionmaker(bind=engine, autocommit=True))

def get(user_id):
    """
    Get a user by id

    :param user_id:
    :return: a user
    """
    return session.query(User).filter(
        User.id == user_id
    ).one()