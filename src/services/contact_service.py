from typing import List
from db import ContactsRepository
from entities import Contact
from common import Result, CustomStatus


class ContactService:
    _MaybeContactsType = List[Contact] | List[None]
    
    def __init__(self, repo: ContactsRepository) -> None:
        self.repo = repo
    
    def all(self) -> Result[_MaybeContactsType]:
        try:
            contacts = self.repo.all()
            return Result[ContactService._MaybeContactsType].success(contacts, CustomStatus.OK)
        
        except Exception as e: # Future: log errors
            print(f"Unexpected error (partial handled): {e}")
            return Result[ContactService._MaybeContactsType].failure(str(e), CustomStatus.UNEXPECTED_ERROR)
    
    def get(self, id: int) -> Result[Contact]:
        try:
            contact = self.repo.get(id)
            if not contact:
                return Result[Contact].failure(f"Contact with id {id} do not exists.", CustomStatus.DB_NOT_EXISTS)
            return Result[Contact].success(contact, CustomStatus.OK)
        
        except Exception as e: # Future: log errors
            print(f"Unexpected error (partial handled): {e}")
            return Result[Contact].failure(str(e), CustomStatus.UNEXPECTED_ERROR)

    def add(self, tag: str, phone: str) -> Result[Contact]:
        try:
            c = Contact(
                tag,
                phone
            )
            new_c = self.repo.add(c)
            return Result[Contact].success(new_c, CustomStatus.CREATED)
            
        except ValueError as e:
            print(f"Error: invalid contact: {e}")
            return Result.failure(str(e), CustomStatus.VALIDATION_ERR)
            
        except Exception as e: # Future: log errors
            print(f"Unexpected error (partial handled): {e}")
            return Result[Contact].failure(str(e), CustomStatus.UNEXPECTED_ERROR)
    
    def delete(self, id: int) -> Result[Contact]:
        try:
            c = self.repo.delete(id)
            
            if not c:
                return Result[Contact].failure(f"Contact with id {id} do not exists.", CustomStatus.DB_NOT_EXISTS)
            return Result[Contact].success(c, CustomStatus.OK)
        
        except Exception as e: # Future: log errors
            print(f"Unexpected error (partial handled): {e}")
            return Result[Contact].failure(str(e), CustomStatus.UNEXPECTED_ERROR)
