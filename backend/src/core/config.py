import os
from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "fastAPI BLog"

    # 数据库配置
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_SERVER: str
    MYSQL_PORT: str
    MYSQL_DB: str

    # 数据库连接池配置
    DB_POOL_SIZE: int = 5  # 连接池大小
    DB_POOL_RECYCLE: int = 3600  # 连接回收时间（秒）
    DB_POOL_TIMEOUT: int = 30  # 连接超时时间（秒）
    DB_ECHO: bool = False  # 是否打印SQL语句（调试用）

    @property
    def DATABASE_URL(self) -> str:
        return f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_SERVER}:{self.MYSQL_PORT}/{self.MYSQL_DB}"

    model_config = ConfigDict(
        env_file=f'.env.{os.getenv("ENVIRONMENT", "dev")}',
        extra='allow'  # 允许额外字段
    )

settings = Settings()
