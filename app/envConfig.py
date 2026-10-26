


from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    
    database_hostname:str
    postgres_db:str
    postgres_user:str
    postgres_password:str
    jwt_secret_key:str
    algorithm:str
    access_token_expires:int

    # class Config():
    #     my_file=".env"
        
    model_config = SettingsConfigDict(env_file=".env")

settings=Settings()

