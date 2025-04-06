from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_api_key: str
    api_ninja_api_key: str
    batch_size: int = 4

    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file='.env.local',
        env_file_encoding='utf-8'
    )

settings = Settings() # type: ignore