from pydantic import BaseModel, EmailStr
from typing import Optional


class UserEntry(BaseModel):
    name: str
    email: EmailStr
    password: str
    role_id: int
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Amanda Dee",
                "email": "email@mail.com",
                "password": "12345667",
                "role_id": 2
            }
        }


class RoleEntry(BaseModel):
    id: int
    description: str
    
class ClaimsEntry(BaseModel):
    description: str
    active: Optional[str]