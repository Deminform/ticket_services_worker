from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    sqlalchemy_database_url: str
    rmq_login: str
    rmq_password:str
    rmq_host: str
    rmq_port: int 

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
