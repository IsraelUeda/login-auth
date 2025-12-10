from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
#o email é validado como um email correto

class UserCreate(UserBase):
    password: str
#o password é uma string simples

class UserPublic(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
#essa classe é usada para retornar os dados do usuario sem expor a senha

    class Config:
        from_attributes = True
#essa configuração permite que o pydantic crie o modelo a partir de um objeto ORM (sqlalchemy)
