from datetime import datetime, timedelta 
from typing import Optional 

from jose import jwt, JWTError 
from passlib.context import CryptContext 

from app.core.config import settings 

"""
#datetime utilizado para caulcular expiração do token

#typing optional signiciar que o valor pode ser do tipo especificado ou None

# jose objeto com funções de encode(criar o token) e decode(verificar o token)
jwterror mostra qual o erro está acontecendo na verificacão do token

#passlib.context é usado para algoritmosa de hash

app.core.config importa as configurações do projeto (secret key, algoritmo, tempo de expiração dos tokens)
"""
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#usa o bcrypt como o hash, se trocar de algoritmo, o auto trata de reconhecer os hashes antigos

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

#função que recebe a senha em texto puro e retorna a senha hasheada,  cria aleatoriamente idependente se a senha for igual

def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

#password é a senha em texto puro
#hashed_password é a senha hasheada salva no banco
#pwd_context.verify compara as duas senhas e retorna true se forem iguais

def create_access_token(data: dict, expires_in: Optional[int] = None) -> str:
    to_encode = data.copy()

    if expires_in is None:
        expires_in = settings.ACCESS_TOKEN_EXPIRE_MINUTES

    expire = datetime.utcnow() + timedelta(minutes=expires_in)
    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

"""
data: dict → payload que você quer colocar dentro do token.
Ex.: {"sub": user.email, "user_id": user.id}
expires_in: Optional[int] = None → pode passar um tempo customizado em minutos.
Se não passar, usa a config padrão do .env.

to_encode = data.copy()
Faz uma cópia do dicionário data para não alterar o original.
Vamos adicionar mais campos a esse dicionário (como exp).

se o expire não for passado pegao access token expire minutes do settings
expire = agora + duração
"""

def create_refresh_token(data: dict, expires_in: Optional[int] = None) -> str:
    to_encode = data.copy()

    if expires_in is None:
        expires_in = settings.REFRESH_TOKEN_EXPIRE_MINUTES

    expire = datetime.utcnow() + timedelta(minutes=expires_in)
    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )
#mesma lógica do access token, mas usando o tempo de expiração do refresh token

def decode_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
        return payload
    except JWTError:
        return None
#tenta decodificar o token usando a secret key e o algoritmo
#se conseguir, retorna o payload (dicionário com os dados dentro do token)
#se der erro (token inválido, expirado, etc), retorna None

