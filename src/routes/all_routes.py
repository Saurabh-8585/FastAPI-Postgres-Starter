from src.routes.users import router as user_route
from fastapi import APIRouter

router = APIRouter()

router.include_router(user_route)
