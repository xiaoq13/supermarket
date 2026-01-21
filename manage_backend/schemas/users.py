from pydantic import BaseModel,ConfigDict
from typing import Optional


class AddUserBase(BaseModel):
    name:str
    telephone:str
    role:str
    address:str
    description:str

class UpdateUserBase(BaseModel):
    name: Optional[str] = None
    telephone: Optional[str] = None
    role: Optional[str] = None
    address: Optional[str] = None
    description: Optional[str] = None
    model_config = ConfigDict(extra="ignore")
