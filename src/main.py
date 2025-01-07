from fastapi import FastAPI
from src.api.v1 import users
from src.db.init_db import init_db
import logging

logger = logging.getLogger(__name__)

app = FastAPI(title="Blog API", description="A simple blog api", version="1.0.0")

@app.on_event("startup")
async def startup_event():
	try:
		init_db()
		logger.info("Database initialized successfully on startup")
	except Exception as e:
		logger.error(f"Failed to initialized database: {e}")

app.include_router(users.router, prefix="/api/v1")
