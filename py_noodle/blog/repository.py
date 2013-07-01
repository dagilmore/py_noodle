__author__ = 'dagilmore'

from database import engine
from sqlalchemy.orm import scoped_session, sessionmaker
from py_noodle.blog.models import Post

# create a Session
session = scoped_session(sessionmaker(bind=engine, autocommit=True))


def save(post):
    """
    Save a post
    :param post:
    :return:
    """
    session.add(post)
    session.flush()

def delete(post):
    """
    Delete a post
    :param Post:
    """
    session.delete(post)
    session.flush()

def delete_post_by_title(title):
    """
    Delete a post by title
    :param title:
    """
    session.query(Post).filter(Post.title == title).delete()

def delete_post_by_id(id):
    """
    Delete a post by id
    :param id:
    """
    session.query(Post).filter(Post.id == id).delete()

def list_all_posts(limit=None):
    """
    List all posts
    :param limit:
    :return: A list of posts
    """
    if limit:
        return session.query(Post).limit(limit)
    else:
        return session.query(Post).all()

def get_posts_by_category(category, limit=None):
    """
    List posts of a certain category
    :param category:
    :param limit:
    :return: A list of posts
    """
    if limit:
        return session.query(Post).filter(Post.category == category).limit(limit)
    else:
        return session.query(Post).filter(Post.category == category)

def get_post_by_title(title):
    """
    Find a post by title
    :param title:
    :return: A post
    """
    return session.query(Post).filter(Post.title == title).first()

