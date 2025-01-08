import sys
import os
from pathlib import Path

# 获取项目根目录
ROOT_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(ROOT_DIR))

from src.db.session import engine, SessionLocal
from sqlalchemy import text
import logging

logger = logging.getLogger(__name__)

def test_db_connection():
    """测试数据库连接"""
    try:
        # 测试直接连接
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            logger.info("Database connection successful!")
            logger.info(f"Result: {result.fetchone()}")
            
        # 测试会话创建
        db = SessionLocal()
        try:
            result = db.execute(text("SHOW TABLES"))
            tables = result.fetchall()
            logger.info("Session created successfully!")
            logger.info(f"Current tables in database: {tables}")
        finally:
            db.close()
            
        return True
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    test_db_connection()