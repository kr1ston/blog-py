from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional

class Settings(BaseSettings):
	PROJECT_NAME: str = 'Blog API'
	VERSION: str = '1.0.0'
	API_V1_STR: str = '/api/v1'

	DATABASE_URL: str

	SECRET_KEY: str
	ALGORITHM: str = 'HS256'
	ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

	class Config:
		env_file = '.env'
		case_sensitive = True

@lru_cache
def get_settings() -> Settings:
	return Settings()