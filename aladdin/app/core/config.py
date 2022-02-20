from typing import List, Union

from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = 'aladdin'
    BACKEND_CORS_ORIGINS: List[str] = ['http://localhost:8000', 'https://localhost:8000', 'http://localhost', 'https://localhost']

    

settings = Settings()
