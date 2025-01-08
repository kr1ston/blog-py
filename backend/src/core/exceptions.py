from fastapi import HTTPException


class BlogException(HTTPException):
    """基础异常类"""

    def __init__(
        self,
        message: str,
        error_code: str,
        status_code: int = 500,
        details: str = None,
    ):
        super().__init__(status_code=status_code)
        self.message = message
        self.error_code = error_code
        self.details = details

class DatabaseError(BlogException):
    """数据库错误"""

    def __init__(self, message: str = "Database error", details: str = None):
        super().__init__(
            message=message,
            error_code="E1002",
            details=details,
        )
