from typing import List
from db import ContactsRepository
from entities import Contact
from common import Result


class ContactService:
    _MaybeContactsType = List[Contact] | List[None]
    _MaybeContactType = Contact | None
    
    def __init__(self, repo: ContactsRepository) -> None:
        self.repo = repo
    
    def all(self) -> Result[_MaybeContactsType]:
        try:
            contacts = self.repo.all()
            return Result[ContactService._MaybeContactsType].success(contacts)
        
        except Exception as e: # Future: log errors
            print(f"Unexpected error (partial handled): {e}")
            return Result[ContactService._MaybeContactsType].failure(str(e))
    
    def get(self, id: int) -> Result[_MaybeContactType]:
        try:
            contact = self.repo.get(id)
            return Result[ContactService._MaybeContactType].success(contact)
        
        except Exception as e: # Future: log errors
            print(f"Unexpected error (partial handled): {e}")
            return Result[ContactService._MaybeContactType].failure(str(e))

    def add(self, tag: str, phone: str) -> Result[Contact]:
        try:
            c = Contact(
                tag,
                phone
            )
            new_c = self.repo.add(c)
            return Result[Contact].success(new_c)
            
        except Exception as e: # Future: log errors
            print(f"Unexpected error (partial handled): {e}")
            return Result[Contact].failure(str(e))
    
    def delete(self, id: int) -> Result[Contact]:
        try:
            c = self.repo.delete(id)

            if not c:
                return Result[Contact].failure(f"Contact with id {id} do not exists.")
            
            return Result[Contact].success(c)
        
        except Exception as e: # Future: log errors
            print(f"Unexpected error (partial handled): {e}")
            return Result[Contact].failure(str(e))
