from pydantic_settings import BaseSettings
from typing import Optional
class AppConfig(BaseSettings):
    openai_api_key: Optional[str]
    

    class Config:
        env_file = ".env"  