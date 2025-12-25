from datetime import datetime
from typing import Optional

    
class Contact:
    def __init__(self, tag: str, phone: str, id: Optional[int] = None, created_at: Optional[datetime] = None) -> None:
        if not tag:
            raise ValueError("Contact's tag can not be empty.")
        
        if not phone:
            raise ValueError("Contact's phone number can not be empty.")
        
        self.tag = tag
        self.phone = phone
        self.id = id
        self.created_at = created_at
