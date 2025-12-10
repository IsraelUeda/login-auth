from pydantic_settings import BaseSettings
from pydantic import AnyUrl
#pydantic serve para criar uma classe de configurações que le as variaveis, valida tipos e converte do .env
#o anyurl valida se a variavel é uma url

class Settings(BaseSettings):
    #Está herdando base settings que trata qualquer atributo como configuração
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    #envoriment o tipo é string e o default é development
    #debug o tipo é booleano e o default é true
    #para mudar o valor dessas variaveis, basta criar um arquivo .env na raiz do projeto e definir as variaveis lá 


    DATABASE_URL: AnyUrl

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30  # 30 dias

    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()