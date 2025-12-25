from db import ContactsRepository
from .contact_service import ContactService
from flask import g


def use_contact_service() -> ContactService:
    if "contact_service" not in g:
        repo = ContactsRepository()
        g.contact_service = ContactService(repo)
    return g.contact_service
