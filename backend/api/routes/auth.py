from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.user import User
from backend.schemas.user import UserCreate, UserResponse
from backend.core.database import get_db
from backend.dependencies.auth import hash_password, verify_password, create_access_token
from backend.core.logger_config import logger
from backend.core.templates import templates

auth_router = APIRouter(prefix="/auth", tags=["Аутентификация и регистрация"])

# Показываем страницу регистрации
@auth_router.get("/register", summary="Страница регистрации", include_in_schema=False)
async def register_page(request: Request):
    return templates.TemplateResponse("pages/register.html", {"request": request})

@auth_router.post("/register", response_model=UserResponse, summary="Регистрация пользователя")
async def register_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    logger.info("Запрос на регистрацию от пользователя")
    existing_user = await db.execute(select(User).where(User.username == user_data.username))
    if existing_user.scalar():
        raise HTTPException(status_code=400, detail="Пользователь уже существует")

    new_user = User(username=user_data.username, hashed_password=hash_password(user_data.password))
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

# Показываем страницу входа
@auth_router.get("/login", summary="Страница входа", include_in_schema=False)
async def login_page(request: Request):
    return templates.TemplateResponse("pages/login.html", {"request": request})

@auth_router.post("/login", response_model=dict, summary="Авторизация пользователя")
async def login_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == user_data.username))
    user = result.scalar()

    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Неверные учетные данные")

    access_token = create_access_token({"sub": str(user.id), "username": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
