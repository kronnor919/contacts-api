from typing import List
from db import ContactsRepository
from entities import Contact
from common import HTTPResult, HTTPStatus


class ContactService:
    _MaybeContactsType = List[Contact] | List[None]
    _MaybeContactType = Contact | None
    
    def __init__(self, repo: ContactsRepository) -> None:
        self.repo = repo
    
    def all(self) -> HTTPResult[_MaybeContactsType]:
        try:
            contacts = self.repo.all()
            return HTTPResult[ContactService._MaybeContactsType].success(contacts, HTTPStatus.OK)
        
        except Exception as e: # Future: log errors
            print(f"Unexpected error (partial handled): {e}")
            return HTTPResult[ContactService._MaybeContactsType].failure(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)
    
    def get(self, id: int) -> HTTPResult[Contact]:
        try:
            contact = self.repo.get(id)
            if not contact:
                return HTTPResult[Contact].failure(f"Contact with id {id} do not exists.", HTTPStatus.NOT_FOUND)
            return HTTPResult[Contact].success(contact, HTTPStatus.OK)
        
        except Exception as e: # Future: log errors
            print(f"Unexpected error (partial handled): {e}")
            return HTTPResult[Contact].failure(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)

    def add(self, tag: str, phone: str) -> HTTPResult[Contact]:
        try:
            c = Contact(
                tag,
                phone
            )
            new_c = self.repo.add(c)
            return HTTPResult[Contact].success(new_c, HTTPStatus.CREATED)
            
        except ValueError as e:
            print(f"Error: invalid contact: {e}")
            return HTTPResult.failure(str(e), HTTPStatus.BAD_REQUEST)
            
        except Exception as e: # Future: log errors
            print(f"Unexpected error (partial handled): {e}")
            return HTTPResult[Contact].failure(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)
    
    def delete(self, id: int) -> HTTPResult[Contact]:
        try:
            c = self.repo.delete(id)
            
            if not c:
                return HTTPResult[Contact].failure(f"Contact with id {id} do not exists.", HTTPStatus.NOT_FOUND)
            return HTTPResult[Contact].success(c, HTTPStatus.OK)
        
        except Exception as e: # Future: log errors
            print(f"Unexpected error (partial handled): {e}")
            return HTTPResult[Contact].failure(str(e), HTTPStatus.INTERNAL_SERVER_ERROR)
