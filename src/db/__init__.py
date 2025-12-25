from flask import Flask
from .db import db, close_db, get_db
from .models import ContactModel
from .repository import ContactsRepository


def init_db(app: Flask) -> None:
    db.init_app(app)
    with app.app_context():
        db.create_all()
        app.teardown_appcontext(close_db)
