from pydantic import BaseModel, EmailStr


class LoginSchema(BaseModel):
    email: EmailStr
    password: str
#o email é validado como um email correto
#o password é uma string simples
#essa classe é usada para receber os dados de login do usuario

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
#essa classe é usada para retornar os tokens gerados após o login

class RefreshSchema(BaseModel):
    refresh_token: str
#essa classe é usada para receber o token de refresh quando o access token expirar