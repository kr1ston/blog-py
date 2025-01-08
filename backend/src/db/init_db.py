import logging
from .session import engine
from .base import Base
from src.models.user import User
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

def init_db() -> None:
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {str(e)}")
        raise

def init_admin(db: Session) -> None:
    """初始化管理员账户"""
    admin = db.query(User).filter(User.username == 'admin').first()
    if not admin:
        admin = User(
            username="admin",
            email="admin@example.com",
            password="admin123",
            is_superuser=True
        )
        db.add(admin)
        try:
            db.commit()
            logger.info("添加管理员成功")
        except Exception as e:
            db.rollback()
            logger.error(f"发生错误：{e}")
            raise
    else:
        logger.info("已有管理员账号")
