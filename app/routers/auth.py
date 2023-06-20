from fastapi import APIRouter, Depends, status


from app.dependencies.users import get_user_service
from app.exceptions.auth import UserAlreadyExistsException
from app.exceptions.error_handlers.error_result import ErrorResult
from app.services.auth import UserService
from app.schemas.users import UserAuthSchema

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@auth_router.post(
    "/register",
    responses={
        status.HTTP_409_CONFLICT: {
            "model": ErrorResult[UserAlreadyExistsException]
        }
    },
    status_code=status.HTTP_201_CREATED)
async def register_user(user_data: UserAuthSchema, service: UserService = Depends(get_user_service)):
    await service.add_user(user_data)


@auth_router.post("/login")
async def login_user(user_data: UserAuthSchema, service: UserService = Depends(get_user_service)):
    pass






















