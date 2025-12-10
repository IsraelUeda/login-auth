from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from app.db.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    
    email = Column(String(255), unique=True, index=True, nullable=False)
    
    hashed_password = Column(String(255), nullable=False)
    
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

"""
Id = chave primaria
email = unica no sistema usado no login
hashed_password = senha criptografada
is_active = se o usuario está ativo ou não
is_superuser = se o usuario é admin ou não
created_at = data de criação do usuario

"""