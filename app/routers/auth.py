from fastapi import APIRouter, Depends, Response, status


from app.dependencies.users import get_auth_service
from app.exceptions.auth import UserAlreadyExistsException
from app.exceptions.error_handlers.error_result import ErrorResult
from app.services.auth import AuthenticationService
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
async def register_user(user_data: UserAuthSchema, service: AuthenticationService = Depends(get_auth_service)):
    await service.add_user(user_data)


@auth_router.post("/login")
async def login_user(
        response: Response,
        user_data: UserAuthSchema,
        service: AuthenticationService = Depends(get_auth_service)
):
    token = await service.login_user(user_data.email, user_data.password)
    response.set_cookie("booking_access_token", token.access_token, httponly=True)






















