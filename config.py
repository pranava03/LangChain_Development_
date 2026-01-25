from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

class Settings(BaseSettings):
    openai_api_key              : str
    anthropic_api_key           : str
    google_api_key              : str
    huggingfacehub_access_token : str

    model_config = SettingsConfigDict(
        env_file          = ENV_PATH,
        env_file_encoding = "utf-8",
        case_sensitive    = False,
        extra             = "ignore",
    )

_settings: Optional[Settings] = None

def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings

settings = get_settings()

if __name__ == "__main__":
    print(settings.model_dump())
    print(settings.huggingfacehub_access_token)