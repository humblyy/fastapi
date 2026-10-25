


from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    
    database_hostname:str
    database_name:str
    database_username:str
    database_password:str
    jwt_secret_key:str
    algorithm:str
    access_token_expires:int

    # class Config():
    #     my_file=".env"
        
    model_config = SettingsConfigDict(env_file=".env")

settings=Settings()

