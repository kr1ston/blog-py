import sys
import os
from sqlalchemy import text
import logging
from typing import Generator

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from src.db.session import engine, get_db
from src.db.init_db import init_db

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_db_connection():
    """测试数据库连接"""
    try:
        # 测试直接连接
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            assert result.scalar() == 1
            logger.info("Database connection successful!")
            
        # 测试会话创建和依赖注入
        db_generator = get_db()
        db = next(db_generator)
        try:
            result = db.execute(text("SHOW TABLES"))
            tables = result.fetchall()
            logger.info("Session created successfully!")
            logger.info(f"Current tables in database: {tables}")
        finally:
            try:
                next(db_generator)
            except StopIteration:
                pass
            
        return True
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        return False

def test_db_initialization():
    """测试数据库初始化"""
    try:
        init_db()
        logger.info("Database initialization successful!")
        return True
    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        return False

if __name__ == "__main__":
    # 测试数据库连接
    assert test_db_connection(), "Database connection test failed"
    
    # 测试数据库初始化
    assert test_db_initialization(), "Database initialization test failed"
    
    logger.info("All database tests passed successfully!") 