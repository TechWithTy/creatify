from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class CreatifyConfig(BaseSettings):
    """
    Creatify API configuration settings.
    """
    CREATIFY_API_KEY: str
    CREATIFY_API_BASE: str = "https://api.creatify.ai/v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        case_sensitive=True,
        extra="ignore",  # Ignore unrelated env vars during settings parsing
    )

@lru_cache()
def get_settings() -> CreatifyConfig:
    """Lazily construct settings to avoid import-time validation."""
    return CreatifyConfig()
