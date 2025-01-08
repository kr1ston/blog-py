from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
import logging

from .exceptions import BlogException, DatabaseError

logger = logging.getLogger(__name__)

def setup_exception_handlers(app: FastAPI) -> None:
    
    @app.exception_handler(BlogException)
    async def blog_exception_handler(request: Request, exc: BlogException):
        """处理所有自定义异常"""
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error_code": exc.error_code,
                "message": exc.message,
                "details": exc.details
            }
        )

    @app.exception_handler(IntegrityError)
    async def integrity_error_handler(request: Request, exc: IntegrityError):
        """处理数据库完整性错误"""
        error_msg = str(exc)
        logger.error(f"Database integrity error: {error_msg}")
        
        if "Duplicate entry" in error_msg:
            if "users.email" in error_msg:
                raise BlogException(message="该邮箱已被注册")
            elif "users.username" in error_msg:
                raise BlogException(message="该用户名已被使用")
        
        raise DatabaseError(details=str(exc))

    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_error_handler(request: Request, exc: SQLAlchemyError):
        """处理 SQLAlchemy 错误"""
        logger.error(f"Database error: {exc}")
        raise DatabaseError(details=str(exc)) 