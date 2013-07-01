__author__ = 'dagilmore'

import py_noodle.blog as blog


def save(form):
    p = blog.models.Post(
        title=form['title'],
        slug=form['slug'],
        category=form['category'],
        body=form['body'],
    )
    blog.repository.save(p)