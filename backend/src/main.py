from fastapi import FastAPI
from src.core.handlers import setup_exception_handlers
from src.api.v1 import users
from src.db.init_db import init_db, init_admin
from src.db.session import SessionLocal
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI(title="Blog API", description="A simple blog api", version="1.0.0")

@app.on_event("startup")
async def startup_event():
	try:
		init_db()
		logger.info("Database initialized successfully on startup")
	except Exception as e:
		logger.error(f"Failed to initialized database: {e}")

	db = SessionLocal()
	try:
		init_admin(db);
	except Exception as e:
		logger.error(f"Failed to initialized database: {e}")
	finally:
		db.close()

# 注册异常处理器
setup_exception_handlers(app)

app.include_router(users.router, prefix="/api/v1")
