from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
    PROJECT_NAME: str = "FASTAPI MYSQL"