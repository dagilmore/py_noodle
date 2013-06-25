__author__ = 'dagilmore'

from database import engine
from sqlalchemy.orm import scoped_session, sessionmaker
from py_noodle.blog.models import Blog

# create a Session
session = scoped_session(sessionmaker(bind=engine, autocommit=True))


def save(blog):
    """

    :param blog:
    :return:
    """
    session.add(blog)

def delete(blog):
    """
    Delete a blog
    :param Blog:
    """
    session.delete(blog)

def delete_blog_by_title(title):
    """
    Delete a blog by title
    :param title:
    """
    session.query(Blog).filter(Blog.title == title).delete()

def delete_blog_by_id(id):
    """
    Delete a blog by id
    :param id:
    """
    session.query(Blog).filter(Blog.id == id).delete()

def list_all_blogs(limit=None):
    """
    List all blogs
    :param limit:
    :return: A list of blogs
    """
    if limit:
        return session.query(Blog).limit(limit)
    else:
        return session.query(Blog).all()

def get_blogs_by_category(category, limit=None):
    """
    List blogs of a certain category
    :param category:
    :param limit:
    :return: A list of blogs
    """
    if limit:
        return session.query(Blog).filter(Blog.category == category).limit(limit)
    else:
        return session.query(Blog).filter(Blog.category == category)

def get_blog_by_title(title):
    """
    Find a blog by title
    :param title:
    :return: A blog
    """
    return session.query(Blog).filter(Blog.title == title).first()

