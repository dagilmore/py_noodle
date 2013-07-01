__author__ = 'dagilmore'

from flask_login import LoginManager
from py_noodle.users import repository

login_manager = LoginManager()
ROLE_USER = 0
ROLE_ADMIN = 1

@login_manager.user_loader
def load_user(userid):
    return repository.get(userid)
