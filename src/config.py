from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    api_ninja_api_key: str

    class Config:
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings() # type: ignore