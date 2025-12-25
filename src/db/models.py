from .db import db
from datetime import datetime
from entities import Contact


class ContactModel(db.Model):
    __tablename__ = "contacts"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    
    def to_entity(self) -> Contact:
        return Contact(
            self.tag,
            self.phone,
            self.id,
            self.created_at
        )
