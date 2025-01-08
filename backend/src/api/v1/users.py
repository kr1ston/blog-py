from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.db.session import get_db
from src.models.user import User
from src.schemas.user import UserCreate, UserResponse, UserUpdate
from src.core.exceptions import BlogException

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """创建用户"""
    if db.query(User).filter(User.username == user.username).first():
        raise BlogException(message="该用户名已被使用")

    if db.query(User).filter(User.email == user.email).first():
        raise BlogException(message="该邮箱已被注册")

    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("", response_model=List[UserResponse])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """获取用户列表"""
    users = db.query(User).offset(skip).limit(limit).all()
    return users


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """获取单个用户"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise BlogException(f"User {user_id} not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    """ "更新用户信息"""
    db_user = db.query(User).filter(user_id == User.id).first()
    if not db_user:
        raise BlogException("找不到该用户")

    if user_update.username and user_update.username != db_user.username:
        raise BlogException(message="该用户名已被使用")

    update_data = user_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """删除用户"""
    db_user = db.query(User).filter(user_id == User.id).first()
    if not db_user:
        raise BlogException("找不到该用户")
    if db_user.username == 'admin':
        raise BlogException("管理员不允许删除")

    db.delete(db_user)
    db.commit()
    return None
    