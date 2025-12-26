from typing import List
from .db import get_db
from .models import ContactModel
from entities import Contact


class ContactsRepository:
    def __init__(self) -> None:
        self.db = get_db()
    
    def all(self) -> List[Contact] | List[None]:
        users = self.db.query(ContactModel).all()
        
        return [u.to_entity() for u in users]
    
    def get(self, id: int) -> Contact | None:
        user = self.db.get(ContactModel, id)
        
        if not user:
            return None
        
        return user.to_entity()
    
    def add(self, c: Contact) -> Contact:
        m = ContactModel(
            tag=c.tag,
            phone=c.phone
        )
        self.db.add(m)
        self.db.commit()
        
        return m.to_entity()

    def delete(self, id: int) -> Contact | None:
        e = self.db.get(ContactModel, id)
        
        if not e:
            return None
        
        self.db.delete(e)
        self.db.commit()
        return e.to_entity()
