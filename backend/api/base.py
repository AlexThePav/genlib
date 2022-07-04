from api.version1.route_users import router as route_users
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(
    router=route_users,
    prefix="/users",
    tags=["users"]
    )
