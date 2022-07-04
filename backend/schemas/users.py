from pydantic import BaseModel
from pydantic import EmailStr


class BaseUser(BaseModel):
    username: str
    email: EmailStr


class UserCreate(BaseUser):
    password: str


class ShowUser(BaseUser):
    is_active: bool

    class Config:
        orm_mode = True
