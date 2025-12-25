from flask_sqlalchemy import SQLAlchemy
from flask import g


db = SQLAlchemy()

def get_db():
    if 'db' not in g:
        g.db = db.session
    return g.db

def close_db(exc=None):
    if 'db' in g:
        db = g.pop("db")
        db.close()
